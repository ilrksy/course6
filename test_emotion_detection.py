"""
Unit tests for the emotion detection module.
"""
import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test suite for the emotion_detector function.
    """

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        """
        Test the emotion_detector function with various expected dominant emotions.
        """
        mock_response_1 = unittest.mock.Mock()
        mock_response_1.status_code = 200
        mock_response_1.text = (
            '{"emotionPredictions": [{"emotion": {"anger": 0.1, "disgust": 0.1, '
            '"fear": 0.1, "joy": 0.9, "sadness": 0.1}}]}'
        )

        mock_response_2 = unittest.mock.Mock()
        mock_response_2.status_code = 200
        mock_response_2.text = (
            '{"emotionPredictions": [{"emotion": {"anger": 0.9, "disgust": 0.1, '
            '"fear": 0.1, "joy": 0.1, "sadness": 0.1}}]}'
        )

        mock_response_3 = unittest.mock.Mock()
        mock_response_3.status_code = 200
        mock_response_3.text = (
            '{"emotionPredictions": [{"emotion": {"anger": 0.1, "disgust": 0.9, '
            '"fear": 0.1, "joy": 0.1, "sadness": 0.1}}]}'
        )

        mock_response_4 = unittest.mock.Mock()
        mock_response_4.status_code = 200
        mock_response_4.text = (
            '{"emotionPredictions": [{"emotion": {"anger": 0.1, "disgust": 0.1, '
            '"fear": 0.1, "joy": 0.1, "sadness": 0.9}}]}'
        )

        mock_response_5 = unittest.mock.Mock()
        mock_response_5.status_code = 200
        mock_response_5.text = (
            '{"emotionPredictions": [{"emotion": {"anger": 0.1, "disgust": 0.1, '
            '"fear": 0.9, "joy": 0.1, "sadness": 0.1}}]}'
        )

        mock_post.side_effect = [
            mock_response_1, mock_response_2, mock_response_3, mock_response_4, mock_response_5
        ]

        result_1 = emotion_detector(
            "I am glad this happened"
        )
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = emotion_detector(
            "I am really mad about this"
        )
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = emotion_detector(
            "I am really disgusted about this"
        )
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = emotion_detector(
            "I am so sad about this"
        )
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(result_5['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
