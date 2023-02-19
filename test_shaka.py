import time
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class PlaybackTest(BaseCase):
    def test_playback(self):
        self.open("https://harmonicinc-com.github.io/shaka-player/latest/demo/#audiolang=en-US;textlang=en-US;uilang=en-US;panel=HOME;build=debug_compiled")

        self.wait_for_element('//button[text()="Play"]', by='xpath')
        self.click('//button[text()="Play"]', by='xpath')
        
        videoEl = self.wait_for_element("video#video")
        
        readyState = videoEl.get_attribute("readyState")
        self.assert_equal(readyState, "0", msg=None)

        self.wait_for_attribute("video#video", "readyState", "4", timeout=4)

        src = videoEl.get_attribute("src")
        self.console_log_string("playing src: " + src)

        secondsToPlay = 2
        time.sleep(secondsToPlay + 1) 

        currentTime = int(float(self.get_attribute("video#video", "currentTime")))
        self.assertTrue(currentTime >= secondsToPlay, msg=None)
