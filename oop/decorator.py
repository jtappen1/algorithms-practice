from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def apply(self, image):
        pass

# ConcreteComponent
class BaseImage(Filter):
    def apply(self, image):
        return image

# Decorator
class FilterDecorator(Filter):
    def __init__(self, wrapped: Filter):
        self._wrapped = wrapped

    def apply(self, image):
        return self._wrapped.apply(image)
    
# Concrete Decorator
class GrayscaleFilter(FilterDecorator):
    def apply(self, image):
        result = super().apply(image)
        return f"Grayscale({result})"

class BlurFilter(FilterDecorator):
    def apply(self, image):
        result = super().apply(image)
        return f"Blur({result})"

def editor():
    image = "photo"
    filtered = GrayscaleFilter(BlurFilter(BaseImage()))
    print(filtered.apply(image))

######################################################################################################################################################################################################
# Stackable text editor

class Text(ABC):

    @abstractmethod
    def transform(self, text):
        pass

class BaseText(Text):
    def transform(self, text):
        return text
    
class TextDecorator(Text):
    def __init__(self, wrapped: Text):
       self._wrapped = wrapped

    def transform(self, text):
        return self._wrapped.transform(text)

class BoldDecorator(TextDecorator):
    def transform(self, text):
        result = super().transform(text)
        return f"<b>{result}<b>"

class ItalicsDecorator(TextDecorator):
    def transform(self,  text):
        result = super().transform(text)
        return f"<i>{result}<i>"

def text_editor():
    text = "HeLLOOOOO World"
    decorated_text = ItalicsDecorator(BoldDecorator(BaseText()))
    print(decorated_text.transform(text))

if __name__ == "__main__":
   text_editor()
   editor()

