from transformers import pipeline, BartForSequenceClassification, AutoTokenizer
import json

class ZeroShot:
    def __init__(self, model_id, json_data_path, cache_dir = None) -> None:
        self.task = "zero-shot-classification"
        self.model_id = model_id
        self.cache_dir = cache_dir
        self.json_data_path = json_data_path
        self.model = BartForSequenceClassification.from_pretrained(
            self.model_id, cache_dir=self.cache_dir)
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_id, cache_dir=self.cache_dir)
        self.classifier = pipeline(
            self.task, model=self.model, tokenizer=self.tokenizer)

    def classify(self, sequence, labels):
        return self.classifier(sequence, labels)

    def load_conversation(self):
        with open(self.json_data_path) as conversation:
            return json.load(conversation)
        
    def test_conversation(self):
        conversations = self.load_conversation()
        for conversation in conversations:
            category = self.classify(conversation["text"], ["greeting",  "camera", "color", "storage", "accessory", "payment"])
            sentiment = self.classify(conversation["text"], ["positive", "negative", "neutral"])
            conversation["category"] = {"label": category["labels"][0], "score": category["scores"][0]}
            conversation["sentiment"] = {"label": sentiment["labels"][0], "score": sentiment["scores"][0]}
            print(conversation)
        return conversations
