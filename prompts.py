"""
This file contains all the instructions used in the CLiC-it 2024 paper,
"To Click it or not to Click it: An Italian Dataset for Neutralizing Clickbait Headlines" 
authored by Daniel Russo, Oscar Araque, and Marco Guerini. 
"""


AUTHOR_COMPONENT = """I have a clickbait headline and its corresponding article, both written in Italian. The clickbait headline \
typically omits key information to create a curiosity gap for the reader. Your task is to extract this missing information, known as a \
"spoiler," from the article's text. The spoiler can be a single keyword, a short text passage, or a list of keywords. Once you have \
identified the spoiler, rewrite the clickbait headline by incorporating this information to eliminate the curiosity gap. The output \
must be in JSON format and written in Italian. The JSON should include two entries: one called "spoiler" that contains the extracted \
spoiler(s), and another called "new_headline" that has the revised headline.

Example Input:

Clickbait headline: "Questo attore ha fatto qualcosa di incredibile sul set di un famoso film!"
Article: "Durante le riprese del film `Il Gladiatore', l'attore Russell Crowe ha deciso di fare un gesto di grande generosità donando una parte significativa del suo stipendio al fondo per i membri della troupe."

Example Output:

{{"spoiler": "Russell Crowe ha donato una parte significativa del suo stipendio al fondo per i membri della troupe",
  "new_headline": "Russell Crowe ha fatto qualcosa di incredibile sul set di 'Il Gladiatore': ha donato una parte significativa del suo stipendio al fondo per i membri della troupe"}}

Please ensure the output is formatted in JSON as specified and that all content is in Italian.

Now do it for the following headline.

Clickbait headline: "{headline}"

Article:"{article}" """


QUESTION_GENERATION = """You will be provided with a clickbait headline written in Italian. Your task is to generate a question that \
addresses any missing or vague information in the headline. Here are some examples:

Headline: Si chiama la benedizione di Dio: rimuove l’alta pressione, il diabete e il grasso nel sangue
Question: Che cosa viene chiamato 'benedizione di Dio'?

Headline: “Emorragia cerebrale”. Italia in apprensione per il suo campione: ricoverato in condizioni gravissime
Question: Chi è il campione?

Please generate the question in Italian, ensuring it seeks to clarify the ambiguous or incomplete details present in the headline.

Headline: "{headline}" """


SPOILER_GEN = """
Ti verranno forniti un titolo clickbait e il suo articolo corrispondente. Il titolo clickbait di solito omette, o non esplicita, \
informazioni chiave per creare curiosità nel lettore. Estrai dall'articolo le informazioni mancanti o vaghe nel titolo che servono per \
colmare questa curiosità. La risposta può essere un messaggio estremamente coinciso oppure un elenco.
Formatta la risposta nel seguente modo. "Risposta: <output>"

Titolo: {headline}

Articolo: {article} """


SPOILER_GEN_QA = """Ti verrà fornita una domanda e un documento. Trova nel documento le informazioni per rispondere alla domanda. La \
risposta può essere un messaggio conciso oppure un elenco.
Formatta la risposta nel seguente modo. "Risposta: <output>"

Domanda: {question}

Documento: {document} """


NEUTRALISATION = """Ti verrano forniti due testi: un titolo clickbait e un testo, chiamato spoiler, che contiene le informazioni \
mancanti nel titolo. Il tuo compito è di riscrivere il titolo clickbait integrando le informazioni dello spoiler. Il nuovo titolo deve \
essere informativo, privo di toni sensazionalistici, e breve. Se Lo spoiler contine tante informazioni, puoi riassumerle in concetti \
più generali.

Titolo: {headline}

Spoiler: {spoiler} """