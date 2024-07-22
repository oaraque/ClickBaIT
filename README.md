# clickIT
Repository for the Clic-it 2024 paper "To Click it or not to Click it"

# Dataset

The dataset is divided into two main sets.

* Gold set. This set has been manually annotated by two experts.
* Silver set. This set has been automatically annotated by a Llama3 model fine-tuned in the manual annotations.

The table below shows the basic statistics of the dataset.

| Set   | Clickbait (\%) | Non-clickbait (\%) | Total |
|----------------|-------------------------|-----------------------------|----------------|
| Golden         | 698 (53%)              | 629 (47%)                  | 1,327          |
| Silver         | 1,563 (56%)            | 1,224 (44%)                | 2,787          |
| _Total_ | 2,261                   | 1,853                       | 4,114          |

## Read dataset

The dataset is stored in a [JSON lines](https://jsonlines.org/) format.
To read the data files, you can use the following code.

```python
import pandas as pd

df = pd.read_json("clickbait_dataset_gold.jsonl", orient="records", lines=True)
```

## Examples

| Category | Headline                                                                                        | Article                                                                                                                                        | Clickbait | Spoiler                                                                                                                                                                                            | Neutralised title                                                                                                                                      |
|-------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Health            | Frutto o fiore? gustosissima e attraente, una celebrità sulle nostre tavole, sveliamo chi è               | Tutti la conosciamo, immancabile sulle nostre tavole, celebre in tutto il mondo ma misteriosa la sua natura, frutto da gustare o fiore per decorare?... | True               | La fragola                                                                                                                                                                                                  | Fragola: gustosissima e attraente, una celebrità sulle nostre tavole                                                                                            |
| Sport           | ``Emorragia cerebrale''. Italia in apprensione per il suo campione: ricoverato in condizioni gravissime   | Il mondo del calcio è in ansia per le condizioni di Beppe Furino, 76 anni, ex capitano della Juventus tra gli anni ‘70 e ‘80...                         | True               | Beppe Furino, ex capitano della Juventus negli anni '70 e '80, è ricoverato nella Stroke Unit dell'ospedale Santa Croce di Moncalieri a causa di una emorragia cerebrale, ma le sue condizioni sono stabili | Beppe Furino, ex capitano della Juventus, ricoverato in condizioni stabili nella Stroke Unit dell'ospedale Santa Croce di Moncalieri per un'emorragia cerebrale |
| Sport           | ``Sono fidanzata con Chiara, la amo''. Il coming out dell’azzurra arriva dopo la sconfitta alle Olimpiadi | “Chiara, la mia fidanzata, lavora in un chiosco non lontano dal centro tecnico federale di Ostia, dove mi alleno...                                     | True               | Alice Bellandi                                                                                                                                                                                              | Alice Bellandi fa coming out alle Olimpiadi di Tokyo: fidanzata con Chiara                                                                                      |
| Science           | Scoperto un metallo che si auto-ripara. Scienziati sbalorditi                                             | Il recente esperimento ha rivelato un fenomeno straordinario...                                                                                         | True               | Il platino                                                                                                                                                                                                  | Il metallo che si auto-ripara: il platino                                                                                                                       |
| Health            | Una malattia che colpisce 500mila persone                                                                 | Parliamo di una malattia sistemica cronica mediata dal sistema immunitario che interessa circa 1,8 milioni di pazienti...                               | True               | La psoriasi colpisce circa 500 mila persone                                                                                                                                                                 | La psoriasi: una malattia che colpisce circa 500mila persone in Italia                                                                                          |
| Environment       | Zanzare, ecco come eliminarle senza insetticidi                                                           | Con l’arrivo del caldo, anche le zanzare si fanno largo nelle nostre case o nei nostri giardini...                                                      | True               | Per eliminare una volta per tutte le zanzare dalla vostra casa, dovreste acquistare un pipistrello                                                                                                          | Zanzare, ecco come eliminarle senza insetticidi: basta acquistare un pipistrello                                                                                |


# Cite

If you use this data, please cite the following work.

```
TODO: ADD
```
