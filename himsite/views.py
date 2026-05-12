# this file my_intro.txt created by himanshu sharma
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>this is index page using httpresponse <h1>")


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, "about_us.html")


def contact(request):
    return render(request, 'contact_us.html')


def analize(request):
    # first value is input name(used in our html) and secound is default value for this
    form_data_ = request.POST.get('form_data', 'default')
    punc_check = request.POST.get('punc_check', 'no punc check')
    num_check = request.POST.get('num_check', 'no num check')
    char_check = request.POST.get('char_check', 'no char check')
    line_check = request.POST.get('line_check', "no line check")
    space_check = request.POST.get('space_check', 'no space check')
    upper_check = request.POST.get('upper_check', 'no upper check')
    print(f'it is form data = {form_data_}')
    print(punc_check)
    print(char_check)
    print(num_check)
    print(line_check)
    print(space_check)

    if punc_check == 'on':
        punc_list = r''',.:;?%|[}{]'\"?/><*^#$@!&()+=`~'''
        analized_text = ''
        for char in form_data_:
            if char not in punc_list:
                analized_text += char
        form_data_ = analized_text

    if line_check == "on":
        analized_text = ''
        for char in form_data_:
            if char != '\n' and char !='\r':
                analized_text+=char
        form_data_ = analized_text
    if space_check == "on":
        analized_text = ''
        for index, char in enumerate(form_data_):
            if form_data_[index] != ' ' or not form_data_[index - 1] == ' ':
                analized_text += char
        form_data_ = analized_text
    if num_check == 'on':
        analized_text = ''
        num = '1234567890'
        for char in form_data_:
            if char not in num:
                analized_text += char
        form_data_ = analized_text
    if upper_check == 'on':
        form_data_ = form_data_.upper()
    if char_check == 'on':
        form_data_ = len(form_data_)

    if punc_check != 'on' and space_check != 'on' and upper_check != 'on' and line_check != 'on' and num_check != 'on' and char_check != 'on':
        return HttpResponse(f'<h2> ERROR!!! please select operation and try again </h2> <h4>{form_data_}<h4>')
    dict = {'text': form_data_}
    return render(request, 'analized.html', dict)

# def char_counter(request):
#     form_data_ = request.GET.get('form_data','default')
#     char_check = request.GET.get('char_check','tick nhi kiya')
#     analized_text =""
#     dict ={'counter':analized_text}
#     if char_check== "on":
#         for tex in form_data_:
#             analized_text = form_data_.count()
#             return render(request, "analized.html", )
#     else:
#         return HttpResponse('<b>Error due to no text</b>')

# def aboutme(request):
#     with open ("my_intro.txt") as mh:
#         home_doc = mh.read()
#         return HttpResponse(f'{home_doc} <a href = "/">go back<a/>')


# def registered(request):
#     form_data_ = request.GET.get('form_data','default')
#     print(f'It is form data = {form_data_}')
#     return render(request,'registered.html')
