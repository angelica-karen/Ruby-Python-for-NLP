class PagesController < ApplicationController
    def home 
      @heart = `python3 lib/assets/python/lesson1_tokenizer.py`
    end
  end
