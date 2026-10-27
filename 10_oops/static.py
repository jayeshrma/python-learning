class Utlis:
    @staticmethod
    def clearText(text):
        return [item.strip() for item in text.split(",")]
    
raw="Book,  copy,Pen, Notepad"

cleaned=Utlis.clearText(raw)
print(cleaned)