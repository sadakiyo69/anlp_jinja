# ANLP Task using Jinja

## 1. The Task/Domain

The domain for this project, was chosen to be Movie review analysis. The task of the system is to structure prompts, so that an Large Language Model can classify its sentiment (positive - negative - neutral) and moreover, it should try to extract aspects of Movies in the review such as acting, the music, or the plot. 

## 2. What the Jinja Template Does 

The Jinja template found as prompt_template.j2, will firstly build us a prompt out of a single review, secondly the template will list aspects that are to be analyzed, using a macro will list exmaples of few-shot that it formated, in a chosen output format thats reused and not repeated. Moreover, the system loops over both, the list of aspects and the list of few-shots, and add them to the prompt. Lastly, there will be an optional node added, so that if a movie review contains a spoiler.

## 3. Why Jinja is Appropriate for this Problem

Firstly, we can make use of the Jinja loop, that will avoid us manually joining strings. Instead of conventional loops, known from e.g. python, that would be nested in a case of prompts with e.g. spoiler and no rating, we make use of jinja {% if %} blocks. The system will be able to generate in three different output formats from the single template, making it neat to aoiv having seperate prompts and duplicate text. Prompt structure from jinja is far more readbale, compared to actual prompt texts, since it is not scattered across strinc concatenation. Lastly, jinja is able to make changes to be only made once, since the macro, mentioned in 2., keeps the fewshot formatting in one place.
