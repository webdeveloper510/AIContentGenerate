from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
import openai
import os
from langdetect import detect
from googletrans import Translator
import json

@csrf_exempt
def index1(request):
    if request.method=='POST':
        input_text=request.POST.get('alpha')
        if input_text:
            language=detect(input_text)
            text_writer=content_generate(input_text,language)  ### call to function 
            return render(request,'generate.html',{"output":text_writer})
        else:
            return HttpResponse(" Please Enter Some Text")
    else:
        return render(request,'generate.html')
 

                  
def content_generate(input_text,language):
    openai.api_key ="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"     
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Auto Response Generator \n\nUser: {input_text} \n\nAI:\n",
        temperature=0.9,
        max_tokens=1500,
        top_p= 0.9,
        frequency_penalty=1,    
        presence_penalty=1,
    )
    output= response.choices[0].text
    return output

