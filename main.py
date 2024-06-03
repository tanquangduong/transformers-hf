from transformers import AutoTokenizer

# Define the model name. In this case, we're using a pre-trained BERT model for multilingual sentiment analysis
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

# Load the pre-trained tokenizer associated with the model
tokenizer = AutoTokenizer.from_pretrained(model_name)