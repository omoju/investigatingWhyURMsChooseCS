# Analyzing socio-curricular factors that affect the decision to choose CS


This work presents a study investigating socio-curricular factors that lead historically underrepresented students’ retention and attrition in introductory Computer Science at UC Berkeley. The Beauty and Joy of Computing (CS10), an introductory CS course for non-majors and the Structure and Interpretation of Computer Programs (CS61A), an introductory CS course for majors are investigated as critical gateway courses in the introductory to Computer Science pipeline.

To learn about the effects of curriculum on the decision to progress along the computer science pipeline, an indept data analysis was performed on data gathered by the study. Preliminary results show agreement with theoretical predictions and significant improvement over previous efforts. 

The work was done as part of a doctoral study in Computer Science education. 

-----------------------------------------------------------------------------------
| Title    | HipHopathy, A Socio-Curricular Study of Introductory Computer Science |
| -------- | --------------------------------------------------------------------- |
| Author   | Omoju Miller 							                               |
| Advisor  | [Dr. Alice Agogino][Alice] 					                       |
| Degree   | Doctor of Philosophy, Computer Science Education 	                   |
| Date     | Dec 2015								                               |
------------------------------------------------------------------------------------
[Alice]: http://www.me.berkeley.edu/people/faculty/alice-m-agogino


## Install

This project requires Python 2.7 and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [Matplotlib](http://matplotlib.org/)
- [brewer2mpl](https://pypi.python.org/pypi/brewer2mpl/1.4)


In addition, you will need to be able to run an jupyter Notebook to do something similar with your data.


## Run

In a terminal/command window, go to the top-level project directory `investigatingWhyURMsChooseCS/` (that contains this README). Then run:

```jupyter notebook DataAnalysis.ipynb```

## Publication
- [Its Deeper than Rap: Toward Culturally Responsive CS](http://dl.acm.org/citation.cfm?id=2604994)
- [Gaining insights into the effects of culturally responsive curriculum on historically underrepresented students’ desire for computer science](Miller_ASEE_2016_DRAFT.pdf) To be presented at in ASEE 2016

## Data

The dataset that is used in this project is unfortunately not available for mass consumption, as it contains sensitive, *personally identifiable* student data.

The dataset was generate through the use of a survey instrument which contains the following attributes for each data point based on a likert scale of 1 to 5, 1 *strongly disagree* and 5 corresponding to *strongly agree*:

#### Self reported attitudes about CS
- atcs_1 I like to use computer science to solve problems.
- atcs_2 I can learn to understand computing concepts.
- atcs_3 I can achieve good grades (C or better) in computing courses.
- atcs_4 I do not like using computer science to solve problems.
- atcs_5 I am confident that I can solve problems by using computation
- atcs_6 The challenge of solving problems using computer science appeals to me.
- atcs_7 I am comfortable with learning computing concepts.
- atcs_8 I am confident about my abilities with regards to computer science.
- atcs_9 I do think I can learn to understand computing concepts.

#### Gendered belief about CS ability
- atcsgender_1 Women are less capable of success in CS than men.
- atcsgender_2 Women are smarter than men.
- atcsgender_3 Men have better math and science abilities than women.

#### Career driven beliefs about CS
- atcsjob_1 Knowledge of computing will allow me to secure a good job.
- atcsjob_2 My career goals do not require that I learn computing skills.

#### Self reported attitudes about computational thinking
- atct_1 I am good at solving a problem by thinking about similar problems I’ve solved before.
- atct_2 I have good research skills.
- atct_3 I am good at using online search tools.
- atct_4 I am persistent at solving puzzles or logic problems.
- atct_5 I know how to write computer programs
- atct_6 I am good at building things.
- atct_7 I’m good at ignoring irrelevant details to solve a problem.
- atct_8 I know how to write a computer program to solve a problem.

#### Self reported attitudes about CS class belonging
- blg_1 In this class, I feel I belong.
- blg_2 In this class, I feel awkward and out of place.
- blg_3 In this class, I feel like my ideas count.
- blg_4 In this class, I feel like I matter.

#### Self reported beliefs about 
- clet_1 I work well in teams.
- clet_2 I think about the ethical, legal, and social implications of computing.
- cltrcmp_1 I am comfortable interacting with peers from different backgrounds than my own (based on race, sexuality, income, and so on.)
- cltrcmp_2 I have good cultural competence, or the ability to interact effectively with people from diverse backgrounds.

#### Demographics
- gender Could I please know your gender
- major Do you have a declared major?

#### CS mentors and role models
- mtr_1 Before I came to UC Berkeley, I knew people who have careers in Computer Science.
- mtr_2 There are people with careers in Computer Science who look like me.
- mtr_3 I have role models within the Computer Science field that look like me.

#### Prior collegiate CS exposure
- prcs_1 Did you take a CS course in High School?
- prcs_2 Did you have any exposure to Computer Science before UC Berkeley?
- prcs_3 Did a family member introduce you to Computer Science?
- prcs_4 Did you have a close family member who is a Computer Scientist or is affiliated with computing industry?
- prcs_5 Did your high school offer AP CS?

#### Instruments pertaining to data science module
- snap_python I was able to see how computational thinking carries over from Snap! to python
- hiphop_d1 The hip-hop data module made me see how computation can enhance culture
- hiphop_d2 Lyrical analysis gave me a new way to think about computation
- song_ct I was able to build on my pre-existing knowledge about songs to further understand computation


## License

The contents of this repository are covered under the [GNU GENERAL PUBLIC LICENSE](License.md).

