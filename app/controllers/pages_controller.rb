class PagesController < ApplicationController
    def home 
      @heart = `python3 lib/assets/python/lesson1_tokenizer.py`
      @part_of_speech = `python3 lib/assets/python/part_of_speech_tagging.py`
    end
  end
