import json

import pytest
import requests


class TestHW13:
    url = "https://playground.learnqa.ru/api/"
    user_agent_values = [
        "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    ]

    expected = {
        "exp_result_1" : '{"platform": "Mobile", "browser": "No", "device": "Android"}',
        "exp_result_2" : '{"platform": "Mobile", "browser": "Chrome", "device": "iOS"}',
        "exp_result_3" : '{"platform": "Googlebot", "browser": "Unknown", "device": "Unknown"}',
        "exp_result_4" : '{"platform": "Web", "browser": "Chrome", "device": "No"}',
        "exp_result_5" : '{"platform": "Mobile", "browser": "No", "device": "iPhone"}'
    }
    expected_results = [
        (user_agent_values[0],expected["exp_result_1"]),
        (user_agent_values[1],expected["exp_result_2"]),
        (user_agent_values[2],expected["exp_result_3"]),
        (user_agent_values[3],expected["exp_result_4"]),
        (user_agent_values[4],expected["exp_result_5"])
    ]

    @pytest.mark.parametrize('user_agent,expected_result',expected_results)
    def test_check_user_agent(self,user_agent,expected_result):


        response = requests.get(
            self.url+"user_agent_check",
            headers={"User-Agent": user_agent}
            )
        actual_result = \
            '{"platform": "' + response.json()["platform"] +\
            '", "browser": "'+ response.json()["browser"] \
            +'", "device": "'+ response.json()["device"] +'"}'

        print("=======")
        print("expect_res: " + expected_result)
        print("actual: " + actual_result)
        assert expected_result == actual_result, f"Response parameters are NOT correct: {actual_result}"

