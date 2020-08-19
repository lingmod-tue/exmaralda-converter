# EXMARaLDA Converter for Time-Aligned Mulit-Layer Speech Transcriptions
This code converts time-aligned multi-layer speech transcriptions of classroom interactions from EXMARaLDA’s Basic Transcription (exb) format into Tab-Separated-Value (tsv) format for easy access with R or Python.

This code converts data from EXMARaLDA’s Basic Transcription format into a Tab-Separated-Value (tsv) format that can be 
immediately loaded into R or Python. EXMARaLDA is a system that facilitates the annotation of oral corpora and allows 
time-aligned multi-layer annotations of spoken language (www.exmaralda.org/en/). Transcripts that are annotated using 
EXMARaLDA’s Partitur editor can be saved in a variety of formats. However, without further preprocessing none of these 
can be read into data frames in R or Python. This code fills this gap by converting time-aligned speech transcriptions 
from exb format into tsv format.

The output file contains a single EXMARaLDA event per line. It combines tier, speaker, and event information using the 
following columns:

* **Tier-ID**: the tier id that is automatically assigned when a tier is created with the Partitur editor.
* **Type**: the tier type that users define when creating a new tier with the Partitur editor, e.g., T(ranscription), D(escription), A(annotation), etc.
* **Display Name**: the tier name that is displayed in the Partitur editor. By default this is a combination of the speaker abbreviation and tier category (see below).
* **Category**: the tier category that users define when creating a new tier with the Partitur editor, e.g., v(erbal), nv (non-verbal), etc.
* **Speaker-ID**: the speaker id that is automatically assigned when a speaker is added to the speaker table with the Partitur editor.
* **Abbreviation**: the speaker abbreviation is a fixed attribute of the speaker properties in the speaker table. It is defined by the user when adding a new speaker to the speaker table.
* **L1**: the first language(s) of a speaker are an optional attribute of the speaker properties in the speaker table. They can be defined by the user when modifying the speaker table.
* **L2**: the second language(s) of a speaker are an optional attribute of the speaker properties in the speaker table. They can be defined by the user when modifying the speaker table.
* **Languages Used**: the languages a speaker uses within a transcript are an optional attribute of the speaker properties in the speaker table. They can be defined by the user when modifying the speaker table.
* **Sex**: the speaker sex is a fixed attribute of the speaker properties in the speaker table. It is defined by the user when adding a new speaker to the speaker table.
* **Start**: the start time of the event in milliseconds
* **End**: the end time of the event in milliseconds
* **String**: the event content

## Requirements
* Python 3

## Usage example

To convert files from exb format to tsv format run:

	python main_converter.py INDIR OUTDIR

with
* **INDIR**: input directory containing the exb file(s)
* **OUTDIR**: output directory for the tsv file(s). If the output directory does not exist, it will be created.

Note: Do not run the code referencing a single file, always reference the directory.

## Release History
* 0.0.1
    * Initial release containing full functionality but lacking
	    * some documentation and comments
	    * code clean-up
	    * implementation of tests

## Meta
This code was developed by Zarah Weiss (www.sfs.uni-tuebingen.de/~zweiss/) for the analysis of spoken language in the 
context of the COLD project (www.die-bonn.de/COLD/).

Distributed under the CC BY-NC-SA 4.0 license. Please cite:

* Zarah Weiss (2020): EXMARaLDA Converter for Time-Aligned Mulit-Layer Speech Transcriptions. 

See ``LICENSE`` for more information.



