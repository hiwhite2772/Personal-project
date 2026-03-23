#Hàm xử lý văn bản
def normalize_text(text):
    #Cắt khoảng trắng đầu và cuối
    text = text.strip()
    #Loại bỏ các khoảng cách dư thừa
    text = " ".join(text.split())

    #Viết hoa từ đầu tiên và sau dấu chấm
    sentences = text.split(".")
    normalized_sentences = []
    for sentence in sentences:
        sentence = sentence.strip().capitalize()
        normalized_sentences.append(sentence)
    
    #Nối các câu lại với nhau
    normalized_text = ". ".join(normalized_sentences)
    return normalized_text
    