import wikipedia
def get_wiki_article(article):
    wikipedia.set_lang('ru')
    try:
        return wikipedia.summary(article)
    except wikipedia.WikipediaException:
        return 'не удалось найти информацию по данному запросу'