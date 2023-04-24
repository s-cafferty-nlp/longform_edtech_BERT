import torch
from transformers import BertTokenizer, BertModel, BertForMaskedLM
import pandas as pd
import random
import re
import requests
from tqdm import tqdm


class Longform():
    def __init__(self, tokenizer_name, model_name):
        self.tokenizer = BertTokenizer.from_pretrained(tokenizer_name)
        self.model = BertForMaskedLM.from_pretrained(model_name)


    def multiple_choice(self, text, top_k=2000, offset=500, top_words=10, choices=5):
        original = text
        tokenized_text = self.tokenizer.tokenize(text.lower())
        token_ids = self.tokenizer.convert_tokens_to_ids(tokenized_text)
        token_ids.sort(reverse=True)
        words_list = self.tokenizer.convert_tokens_to_string(self.tokenizer.convert_ids_to_tokens(token_ids)).split()
        words_to_replace = [x for x in words_list if (x in set(text.split())) & (x.isdigit() == False)][:top_words]
        words_to_replace = list(set(words_to_replace))
        sentences = text.split('.')
        processed_sentences = []
        prompt_sentences = []
        answer_list = []
        counter = 1

        for sentence in sentences:
            masked_sentence = []
            prompt_sentence = []
            for word in sentence.split():
                if word in set(words_to_replace):
                    words_to_replace.remove(word)
                    masked_sentence.append('[MASK]')
                    prompt_sentence.append(f'({counter})____________')
                    answer_list.append(f'{counter}. {word}')
                    counter += 1
                else:
                    masked_sentence.append(word)
                    prompt_sentence.append(word)
            
            prompt_sentences.append((' ').join(prompt_sentence))
            processed_sentences.append((' ').join(masked_sentence))

        masked_indices_list = []
        alternatives_list = []
        counter = 0

        for sentence in processed_sentences:
            sentence = "[CLS] %s [SEP]"%sentence
            tokenized_sentence = self.tokenizer.tokenize(sentence)
            masked_indices = [i for i, e in enumerate(tokenized_sentence) if e == '[MASK]']
            masked_indices_list.append(masked_indices)
            indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_sentence)
            tokens_tensor = torch.tensor([indexed_tokens])

            if len(masked_indices) > 0:
                with torch.no_grad():
                    outputs = self.model(tokens_tensor)
                    predictions = outputs[0]
                for masked_index in masked_indices:
                    probs = torch.nn.functional.softmax(predictions[0, masked_index], dim=-1)
                    top_k_weights, top_k_indices = torch.topk(probs, top_k, sorted=True)
                    alternatives = []
                    for i, pred_idx in enumerate(top_k_indices):
                        predicted_token = self.tokenizer.convert_ids_to_tokens([pred_idx])[0]
                        token_weight = top_k_weights[i]
                        alternatives.append(predicted_token)

                    alternatives = [x for x in alternatives if '##' not in x]
                    alternatives = [x for x in alternatives if (x.isalnum()) & (x.isdigit() == False)]
                    alternatives = random.choices(alternatives[offset:],k=choices)
                    alternatives = [answer_list[counter].split()[1]] + alternatives
                    random.shuffle(alternatives)
                    alternatives_list.append(alternatives)
                    counter += 1
        
        letters = ['A. ','B. ','C. ','D. ','E. ','F. ','G. ','H. ']
        
        formatted_answers = []
        for idx, multiple_choice in enumerate(alternatives_list):
            formatted_answers.append(f'{idx+1}.')
            for i, choice in enumerate(multiple_choice):
                formatted_answers.append(letters[i] + choice)
            formatted_answers.append('')

        answer_dictionary = {}
        
        for idx, multiple_choice in enumerate(alternatives_list):
            answer_dictionary[idx] = []
            for i, choice in enumerate(multiple_choice):
                answer_dictionary[idx].append(letters[i] + choice.lower())

        formatted_prompts = []
        answer_number = 0
        for sent in prompt_sentences:
            pattern = re.compile(r"(\(\d+\))")
            answers = re.findall(pattern,sent)
            formatted_prompts.append(sent+'. ')
            if len(answers) > 0:
                for ans in answers:
                    formatted_prompts.append('')
                    formatted_prompts += answer_dictionary[answer_number]
                    answer_number += 1 
                    formatted_prompts.append('')


        # prompt = ('').join(prompt_sentences)

        # results = [prompt] + ['',''] + formatted_answers

        return formatted_prompts, answer_list
    
    def chatGPT(self, text):
        url = "https://api.openai.com/v1/completions"
        headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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",
        }
        data = { 
        "model": "text-davinci-003",
        "prompt": text,
        "max_tokens": 4000,
        "temperature": 1.0,
        }
        response = requests.post(url, headers=headers, json=data)
        output = response.json()['choices'][0]['text']
        
        return output
    
    def generate_longform_questions(self, topics_list, save = True, ans_path='../data/answers.txt', question_path='../data/questions.txt', top_k=2000, offset=500, top_words=10, choices=5):
        question_output = ['AI GENERATED QUESTIONS','']
        answers_output = ['ANSWER SHEET','']

        for idx, topic in tqdm(enumerate(topics_list)):

            prompt = f'Write an essay about {topic}'
            text = self.chatGPT(prompt)
            questions, answers = self.multiple_choice(text,top_k=top_k, offset=offset, top_words=top_words, choices=choices)

            question_output += [f'QUESTION #{idx+1}']
            answers_output += [f'QUESTION #{idx+1}']
            question_output += questions + ['']
            answers_output += answers + ['']

        if save == True:
            with open(question_path, 'w') as fp:
                for item in question_output:
                    fp.write("%s\n" % item)
                

            with open(ans_path, 'w') as fp:
                for item in answers_output:
                    fp.write("%s\n" % item)

        else:
            return question_output, answers_output
    






