# Corpus of Australian and New Zealand Spoken English (CoANZSE)

## Announcement

The dataset has limited access and requires access/download permission from [Harvard Dataverse - Corpus of Australian and New Zealand Spoken English](https://doi.org/10.7910/DVN/GW35AK).

Please acknowledge that the dataset owners are [Steven Coats](https://cc.oulu.fi/~scoats/) and [Jeremy Yuenger](https://www.iq.harvard.edu/people/jeremy-yuenger). This repository is only used for research purposes in [Southern Cross AI](https://github.com/southern-cross-ai) projects.

Any commercial use is not permitted by the dataset owner. Any distribution of this repository is not recommended. For more information, please read `terms.md`, or visit [Harvard Dataverse - Community Norms](https://dataverse.org/best-practices/dataverse-community-norms) and the [original dataset page]( https://doi.org/10.7910/DVN/GW35AK).

## Overview

The [Corpus of Australian and New Zealand Spoken English (CoANZSE)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FGW35AK) is a **196-million-word corpus** of **geolocated automatic speech recognition (ASR) YouTube transcripts** from local government channels in **Australia** and **New Zealand**, created for the study of lexical, grammatical, and discourse-pragmatic phenomena of spoken language, as well as for content and language analysis in digital humanities and social science fields. 

**Annotation** includes **individual word timings** and **video IDs** of transcripts, making it easy to instantly view the video(s) for any given search. The corpus was created from **55,896 ASR transcripts** from **472 YouTube channels**, corresponding to almost **24,007 hours of video**. The size of the corpus is **195,583,873 tokens**. 

The channels sampled in the corpus are associated with local government entities such as **local, city, county, district, and regional councils**, and transcripts are from a range of video types. Recordings of public meetings are well-represented. Related resources are the [Corpus of North American Spoken English](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/X8QJJV) and the [Corpus of British Isles Spoken English](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/UGIIWD).

**Keywords**: Corpus linguistics, Dialectology, Spoken language, Speech transcripts, Australia, New Zealand.

## Data Source

Access to this dataset is granted by [Harvard Dataverse - Corpus of Australian and New Zealand Spoken English (CoANZSE)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FGW35AK). 

The contributors to the current version (5.0) of the dataset are [Steven Coats](https://cc.oulu.fi/~scoats/) and [Jeremy Yuenger](https://www.iq.harvard.edu/people/jeremy-yuenger).

## Dataset Structure

Under `dataset`, there are 5 files inside:

- `metadata.json`: The metadata of the dataset.
- `coanzse_tokens_distributable_02072023.csv.gz`: The 303 MB untagged corpus.
- `coanzse_tokens_distributable_02072023.csv`: The 963 MB unzipped file from `coanzse_tokens_distributable_02072023.csv.gz`.
- `coanzse_textpos_distributable_02072023.csv.gz`: The 1.0 GB PoS-tagged corpus with word timings.
- `coanzse_textpos_distributable_02072023.csv`: The 3.0 GB unzipped file from `coanzse_textpos_distributable_02072023.csv.gz`.

---

The **separator** for both files is the pipe character "|". 

The files have the **columns** 'country', 'state', 'council_name', 'channel_title', 'channel_url', 'video_title', 'video_id', 'upload_date', 'video_length', 'location','nr_words', 'text_pos' (or 'text', in the untagged version), and 'latlong'.

Each **row** corresponds to an individual transcript. 

In order to comply with Fair Use provisions of US copyright law, the original ASR transcript files from YouTube have been transformed into this version of the corpus: **For every 200 words, 10 words have been replaced with "@"**. In the PoS-tagged and word-timed corpus, these tokens have the form @_XX_1.0. See also https://cc.oulu.fi/~scoats/CoANZSE.html.

## License and Terms of Use

Notice that the dataset has customised dataset terms, please visit the [original dataset page](https://doi.org/10.7910/DVN/GW35AK) for more information.

```
License/Data Use Agreement

Our [Community Norms](https://dataverse.org/best-practices/dataverse-community-norms) as well as good scientific practices expect that proper credit is given via citation. Please use the data citation shown on the dataset page.

Custom Dataset Terms — the following Custom Dataset Terms have been defined for this dataset.

Terms of Use 

I. Acceptance of this Agreement

By downloading or otherwise accessing the Materials, Downloader represents his/her acceptance of the terms of this Agreement.

II. Modification of this Agreement

Users may modify the terms of this Agreement at any time. However, any modifications to this Agreement will only be effective for downloads subsequent to such modification. No modifications will supersede any previous terms that were in effect at the time of the Downloader's download.

III. Use of the Materials

Use of the Materials include but are not limited to viewing parts or the whole of the content included in the Materials; comparing data or content from the Materials with data or content in other Materials; verifying research results with the content included in the Materials; and extracting and/or appropriating any part of the content included in the Materials for use in other projects, publications, research, or other related work products.

1. Representations

A. In Use of the Materials, Downloader represents that:

1. Downloader is not bound by any pre-existing legal obligations or other applicable laws that prevent Downloader from downloading or using the Materials;
2. Downloader will not use the Materials in any way prohibited by applicable laws;
3. Downloader has no knowledge of and will therefore not be responsible for any restrictions regarding the use of Materials beyond what is described in this Agreement; and
4. Downloader has no knowledge of and will therefore not be responsible for any inaccuracies and any other such problems with regards to the content of the Materials and the accompanying citation information.

B. Restrictions In his/her Use of the Materials, Downloaders cannot:

1. obtain information from the Materials that results in Downloader or any third party(ies) directly or indirectly identifying any research subjects with the aid of other information acquired elsewhere;
2. produce connections or links among the information included in User's datasets (including information in the Materials), or between the information included in User's datasets (including information in the Materials) and other third-party information that could be used to identify any individuals or organizations, not limited to research subjects; and
3. extract information from the Materials that could aid Downloader in gaining knowledge about or obtaining any means of contacting any subjects already known to Downloader.

IV. Representations and Warranties

USER REPRESENTS THAT USER HAS ALL RIGHTS REQUIRED TO MAKE AVAILABLE AND DISTRIBUTE THE MATERIALS. EXCEPT FOR SUCH REPRESENTATION, THE MATERIALS ARE PROVIDED "AS IS" AND "AS AVAILABLE" AND WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, AND ANY WARRANTIES IMPLIED BY ANY COURSE OF PERFORMANCE OR USAGE OF TRADE, ALL OF WHICH ARE EXPRESSLY DISCLAIMED.

WITHOUT LIMITING THE FOREGOING, USER DOES NOT WARRANT THAT: (A) THE MATERIALS ARE ACCURATE, COMPLETE, RELIABLE OR CORRECT; (B) THE MATERIALS FILES WILL BE SECURE; (C) THE MATERIALS WILL BE AVAILABLE AT ANY PARTICULAR TIME OR LOCATION; (D) ANY DEFECTS OR ERRORS WILL BE CORRECTED; (E) THE MATERIALS AND ACCOMPANYING FILES ARE FREE OF VIRUSES OR OTHER HARMFUL COMPONENTS; OR (F) THE RESULTS OF USING THE MATERIALS WILL MEET DOWNLOADER'S REQUIREMENTS. DOWNLOADER'S USE OF THE MATERIALS IS SOLELY AT DOWNLOADER'S OWN RISK.

V. Limitation of Liability

IN NO EVENT SHALL USER BE LIABLE UNDER CONTRACT, TORT, STRICT LIABILITY, NEGLIGENCE OR ANY OTHER LEGAL THEORY WITH RESPECT TO THE MATERIALS (I) FOR ANY DIRECT DAMAGES, OR (II) FOR ANY LOST PROFITS OR SPECIAL, INDIRECT, INCIDENTAL, PUNITIVE, OR CONSEQUENTIAL DAMAGES OF ANY KIND WHATSOEVER.

VI. Indemnification

Downloader will indemnify and hold User harmless from and against any and all loss, cost, expense, liability, or damage, including, without limitation, all reasonable attorneys' fees and court costs, arising from the i) Downloader's misuse of the Materials; (ii) Downloader's violation of the terms of this Agreement; or (iii) infringement by Downloader or any third party of any intellectual property or other right of any person or entity contained in the Materials. Such losses, costs, expenses, damages, or liabilities shall include, without limitation, all actual, general, special, and consequential damages.

VII. Dispute Resolution

Downloader and User agree that any cause of action arising out of or related to the download or use of the Materials must commence within one (1) year after the cause of action arose; otherwise, such cause of action is permanently barred.

This Agreement shall be governed by and interpreted in accordance with the laws of the Commonwealth of Massachusetts (excluding the conflict of laws rules thereof). All disputes under this Agreement will be resolved in the applicable state or federal courts of Massachusetts. Downloader consents to the jurisdiction of such courts and waives any jurisdictional or venue defenses otherwise available.

VIII. Integration and Severability

This Agreement represents the entire agreement between Downloader and User with respect to the downloading and use of the Materials, and supersedes all prior or contemporaneous communications and proposals (whether oral, written or electronic) between Downloader and User with respect to downloading or using the Materials. If any provision of this Agreement is found to be unenforceable or invalid, that provision will be limited or eliminated to the minimum extent necessary so that the Agreement will otherwise remain in full force and effect and enforceable.

IX. Miscellaneous

User may assign, transfer or delegate any of its rights and obligations hereunder without consent. No agency, partnership, joint venture, or employment relationship is created as a result of the Agreement and neither party has any authority of any kind to bind the other in any respect outside of the terms described within this Agreement. In any action or proceeding to enforce rights under the Agreement, the prevailing party will be entitled to recover costs and attorneys' fees.

Restrictions 

The corpus is available for the non-commercial purposes of research, education, and scholarship.
```