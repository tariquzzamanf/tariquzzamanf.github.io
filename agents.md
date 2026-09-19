# Agent instructions — Md. Tariquzzaman’s academic website

This is the single maintained Markdown guide for this project. Read it before making changes, follow it during development, and update it as the project evolves.

## Working agreement and source priority

- Follow the user’s latest instructions first. Record durable decisions here when they change content, design, or the development workflow.
- The PDF and LaTeX CV in `files/cv/` are the primary factual sources. The content inventory below is secondary and may contain older descriptions; the current approved page sources and explicit user corrections take precedence over that inventory.
- Do not invent dates, publication status, personal interests, or research claims. Preserve author order and distinguish accepted work from preprints.
- Maintain this document in place; do not create additional Markdown guides unless requested. Update affected sections rather than accumulating contradictory notes or a transcript of every edit.
- Keep generated HTML synchronized with its source. Check the relevant page after layout changes, including small screens where applicable.
- Keep project work inside this directory. Check the Git root before staging or publishing; this folder was previously inside a parent home-directory working tree.
- Do not publish or push until the user requests it.

## Approved design and content decisions

- Use warm cream paper, ebook-like serif typography (Bookerly when installed, bundled Literata otherwise), muted green accents, subtle colored borders, polished buttons, and restrained hover motion.
- Preserve the five pages: Home, Research, Publications, CV, and Personal. Avoid generic slogans and decorative topic straplines.
- Home: retain the two approved biography paragraphs in `content/home.html`. Put role, institution, and location below the portrait rather than repeating them in the opener. Keep the desktop biography visibly larger (currently 19px) and align its action row with the bottom of the portrait and caption where space allows.
- Home: keep research-interest cards and the personal section. Do not add a milestones/news section or a selected-publications section.
- Research: use exactly “Low-resource NLP”, “Evaluation & bias”, “Accessibility”, and “Research community” for the contents links and matching section headings. Organize the work around concrete papers using the CV, with brief descriptions and resource links. Avoid redundant subtitles; paper titles must be smaller than section headings.
- Research: keep all sticky contents links visible below the sticky site header while scrolling.
- Publications: use large metrics in four columns (publication count, citations, h-index, i10-index) directly below the page title and lead, with Google Scholar and Full CV (PDF) actions. Keep the metrics on the page background without a surrounding box, border, or surface fill. Never invent metrics; maintain verified values in `content/scholar-metrics.json` and display unavailable values as dashes with an explanatory note. Group papers into Journal articles, Conference papers, Workshop & shared-task papers, and Preprints, using J/C/W/P numbering, area tags, and a sticky contents sidebar with scroll-driven active highlighting. Keep Code & data and existing paper anchors. On phones, use compact sticky section links below the header.
- Research, Publications, CV, and Personal: share the “On this page” navigation style, sticky placement below the site header, scroll-driven active-section highlighting, and compact sticky links on phones.
- CV: retain only the approved appointments in the current CV; do not restore removed employment entries from older sources. Group teaching by course with semesters in brackets; keep course names at a restrained 16px, smaller than section headings. Spell out “Relational Database Management Systems Lab”.
- Personal: use Anime, Movies, Books, and Sports in that order, with topic navigation and the introduction “A few things about me that the CV does not cover. Pick a topic on the left.” Display the owner’s supplied favorites in their given order, with remotely hosted artwork and source links. Anime is “Top 10, all time”; Movies is “All-time favorites · 8 picks,” with a note that it is not a complete watch history. Do not invent additional picks.
- Keep documentation and site content self-contained, without references or attribution to an external design-inspiration website.

## Project and development workflow

A static, reading-focused academic portfolio with warm cream paper, muted green links, and locally hosted Literata. Bookerly is used if installed on a visitor's device; Literata is bundled under the SIL Open Font License in `assets/fonts/OFL.txt`. Content and navigation work without JavaScript; optional JavaScript adds theme and mobile-menu controls. No package installation or external font service is required.

### Preview locally

From this folder:

```sh
python3 scripts/build.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765. Stop the server with Ctrl+C. If the port is occupied, use another number. You can also open `index.html` directly.

### Editing

- `content/home.html`, `content/research.html`, `content/cv.html`, `content/personal.html`: page content.
- `content/publications.json`: publication metadata, author order, status, and resource links.
- `content/personal.json`: ordered personal favorites, artwork URLs, and source links.
- `content/news.json`: dated updates; the text field allows HTML links.
- `content/teaching.json`: courses grouped by academic term.
- `scripts/build.py`: shared layout, publication rendering, metadata, and publications page introduction.
- `assets/style.css`: typography, spacing, and page layouts.
- `assets/interactions.css`: button styles, theme colors, borders, hover/focus states, and reduced-motion support.
- `assets/app.js`: optional theme toggle and mobile navigation, including Escape to close the menu.
- `profile.jpg`: supplied portrait.
- `files/cv/tariq.pdf`: current downloadable CV.

After editing content or templates, run `python3 scripts/build.py`. Commit the generated root-level HTML pages along with their sources. CSS changes do not need a rebuild.

### Publish later on GitHub Pages

1. Put this folder's contents in your repository named `tariquzzamanf.github.io` and push them to its `main` branch.
2. In repository **Settings → Pages**, select **Deploy from a branch**, then **main** and **/ (root)**, and save.
3. The site will be available at https://tariquzzamanf.github.io/ after deployment finishes.

The generated HTML and `.nojekyll` support branch-based publishing without a build service. URLs are relative so the draft also works from a local folder. No deployment has been performed.

This folder is now a dedicated Git repository with origin `git@github.com:tariquzzamanf/tariquzzamanf.github.io.git`. Verify the Git root before staging or publishing; do not stage or push the parent home-directory repository.

The user-requested `readme.md` documents this website. `github-profile/readme.md` is the prepared README for the separate `tariquzzamanf/tariquzzamanf` profile repository; copy it to that repository's root as `README.md` when publication is requested. Keep its biography and research descriptions consistent with the approved website sources.

### Content provenance and remaining details

The PDF and LaTeX CV in `files/cv/` are primary; The content inventory below supplies secondary biography, author names, teaching, news, and resource links. The design guidance in this document governs presentation. Publication status is preserved from the CV: Findings of ACL 2026 is explicitly **accepted**, and BDA is a **preprint**. External publication statuses have not been independently updated.

The source CV contains placeholders for the SSL start date and graduate research topic. Those placeholders are omitted from the HTML and remain only where present in the editable source. Academic teaching terms are retained as supplied, including 2023–2024; they have not been inferred from the appointment date.

The Personal page lists the owner’s supplied favorites in `content/personal.json`, rendered through `content/personal.html`. Artwork URLs point directly to Kitsu, Wikimedia, and Open Library; do not store cover binaries in the repository. Remote hosting does not imply a copyright license. Keep the source links and rights-holder note. Fullmetal Alchemist currently uses the original series cover.

## Design philosophy

Build an original academic website with clear information architecture, a reading-focused visual language, and content grounded in the owner’s actual work.

### Start with the visitor's questions

The site should make it easy to understand who the person is, what they work on, what they have produced, and how to contact them. Readers should be able to skim for an overview or follow links into detail without learning an unusual navigation system.

Give each page a distinct purpose. Keep a small, consistent primary navigation, use recognizable page names, and make the current location apparent.

### Page organization to carry forward

| Page | Purpose | Content organization |
| --- | --- | --- |
| Home | Introduce the person and offer starting points. | Identity and affiliation, a short introduction, research interests and direct contact or professional links. |
| Research | Explain the intellectual agenda and its context. | A short overview, collaborators or mentors where relevant, research experience, and thematic directions supported by selected work. |
| Publications | Provide a reliable, scannable record of outputs. | Clearly grouped publication entries with bibliographic details and links to papers, code, or datasets. Keep publication status explicit. |
| CV | Present the professional and academic record. | Clearly labeled sections for appointments, education, awards, teaching, experience, and relevant skills, with a readily available PDF. |
| Personal | Show interests beyond professional credentials. | Topic-based collections of interests, reading, recommendations, or writing, populated only where there is meaningful content. |

Section order, grouping, and prominence should reflect the owner's actual priorities. Include only useful sections.

#### Home: orientation before detail

Provide enough context to understand the person quickly. Treat research summaries as entry points into deeper pages. Keep the introduction selective so the homepage remains useful as the rest of the site grows.

#### Research: themes connected to evidence

Explain the questions and motivations that connect individual projects. Associate each theme with relevant work so readers can move from an accessible explanation to concrete evidence. Give collaborators and experience context without letting them obscure the research itself.

#### Publications: consistent records

Use a repeatable reading order for titles, authors, venues, dates, and resource links. Group papers by publication type and include code and dataset links. Readers should be able to distinguish published work and preprints without relying on color.

#### CV: easy retrieval

Make the page useful for someone looking for a particular qualification or period of experience. Use consistent dates and entry structure within clearly named sections. Link to the publication catalog where appropriate, and keep the downloadable CV easy to find.

#### Personal: room for a different tone

Let this page feel more informal while remaining part of the same website. Organize unrelated interests into understandable topics. Use topic navigation and visible sections for the personal collections.

### Navigation at two levels

Global navigation moves between page purposes. Local navigation helps readers move within longer pages. Use a contents list or compact section links for local navigation. Sticky contents must remain fully visible below the site header.

Link related content directly. A homepage interest should lead to its research explanation; a research theme should lead to relevant outputs. Give useful sections stable links so visitors can share a specific destination.

### Visual principles, with freedom of expression

- **Make hierarchy obvious.** Page titles, section headings, main content, metadata, and actions should be distinguishable at a glance.
- **Design for reading.** Use comfortable line lengths, legible text, and spacing that clarifies relationships.
- **Let content determine the format.** A biography, citation, career entry, and personal collection need different treatments within one coherent system.
- **Use emphasis selectively.** Highlight the information that helps visitors understand or act; keep supporting details quieter.
- **Build consistency through repetition.** Similar content should behave predictably across pages, even when individual page layouts differ.

Choose typography, palette, image treatment, layout proportions, spacing rhythm, and decorative details independently. Use cards, badges, borders, icons, and sidebars only where they help readers. A distinct composition and typographic hierarchy will establish more individuality than a color substitution alone.

### Usability and durability

On small screens, preserve the reading order and access to navigation while allowing the composition to change. Interactive elements should support keyboard use, visible focus, readable contrast, and reduced-motion preferences. Verify these requirements when changing the interface.

Keep substantive content available in the initial HTML. Use JavaScript to improve navigation and presentation. Preserve page-specific titles, descriptions, stable URLs, and meaningful link previews so individual pages work as independent entry points.

Keep content separate from presentation so routine updates remain straightforward. The repository's structured content and static generation support this principle; its exact implementation is not part of the visual brief. Use accurate personal records and original wording, and include sections because they serve the owner and readers.

### Review questions for the new design

- Can a first-time visitor quickly identify the person, their work, and a way to contact them?
- Is the difference between Research, Publications, and CV clear?
- Can readers skim long pages and follow a topic into greater detail?
- Does the site have its own recognizable composition and visual identity?
- Does the organization remain useful on a phone and as more content is added?

## Md. Tariquzzaman — content inventory

Standalone content extracted from the existing repository on 2026-09-18. This is source material for a new website, with no inherited styling, templates, or layout requirements. Statements and dates are preserved from the source, not independently verified or updated. “Present” and “in progress” retain their source meaning.

### Identity and contact

- Full name: Md. Tariquzzaman
- Alternate name: Tariq
- Role: Junior Lecturer, Computer Science and Engineering
- Institution: Islamic University of Technology
- Department: Dept. of Computer Science & Engineering
- Institution website: https://www.iutoic-dhaka.edu/
- Website: https://tariquzzamanf.github.io
- Email: tariquzzaman@iut-dhaka.edu
- [Systems and Software Lab (SSL)](https://cse.iutoic-dhaka.edu/ssl)
- Board Bazar, Gazipur 1704, Bangladesh
- Graduate supervisor: [Hasan Mahmud](https://cse.iutoic-dhaka.edu/profile/hasan/education)
- M.Sc. in CSE, IUT (in progress). B.Sc. in CSE, IUT, 2024.
- Email: mailto:tariquzzaman@iut-dhaka.edu
- Scholar: https://scholar.google.com/citations?hl=en&user=LWB_NzwAAAAJ
- GitHub: https://github.com/tariquzzamanf
- HF: https://huggingface.co/aplycaebous
- LinkedIn: https://www.linkedin.com/in/tariquzzamanf/
- Professional identity link: https://cse.iutoic-dhaka.edu/profile/tariquzzaman
- Professional identity link: https://scholar.google.com/citations?hl=en&user=LWB_NzwAAAAJ
- Professional identity link: https://www.linkedin.com/in/tariquzzamanf/
- Professional identity link: https://github.com/tariquzzamanf

### Biography

My work spans low-resource Bangla language processing, harmful content and misinformation detection, sign language instruction generation, and benchmarking scenario-induced bias in large language models. My open releases include informal Bangla FastText embeddings, the BdSLIG sign language dataset, and the BDA augmentation framework.

I am a member of the Systems and Software Lab, where I pursue graduate research under Hasan Mahmud. My undergraduate thesis was supervised by Mohsinul Kabir.

### Research overview

My work centers on language technology for people the field tends to under-serve: speakers of low-resource languages, users of low-resource sign languages, and readers exposed to harmful or misleading text in languages that benchmarks rarely cover.

- Areas of expertise: Natural Language Processing; Bangla NLP; Low-resource language processing; Misinformation detection; Harmful content detection; Sign language instruction generation; LLM evaluation; Human-Centered AI

#### Research interests

- Low-resource & Bangla NLP: Embeddings, augmentation, and modeling for informal Bangla, where clean labelled data is scarce.
- Associated topics / outputs: BLP @ EMNLP 2023; arXiv 2024
- Misinformation & harmful content: Detecting violence-inciting text and financial misinformation across languages and platforms.
- Associated topics / outputs: ACL 2026; BLP @ EMNLP 2023
- Accessibility & sign language: Sign language instruction generation for learners of low-resource sign languages.
- Associated topics / outputs: CV4A11y @ ICCV 2025; BdSLIG
- LLM evaluation & bias: Benchmarks that surface how model judgments shift with persona, region, and identity.
- Associated topics / outputs: MFMD-Scen; 22 models; 4 languages

### Research directions

#### Low-resource & Bangla NLP

Bangla is spoken by over 230 million people and still lacks the clean, labelled, in-domain data that modern methods assume. I build the pieces that close that gap: embeddings trained on the informal Bangla people actually write, and augmentation that stretches small datasets further.

- Related work: [A Novel Informal Bangla FastText Embedding for Violence Inciting Text Detection](https://aclanthology.org/2023.banglalp-1.26/)
- Research description: A custom FastText embedding trained on informal Bangla social media text. Paired with a BiLSTM it reaches near-transformer accuracy while being far faster and cheaper than BanglaBERT. Best Shared Task Paper Award at BLP @ EMNLP 2023.
- Related work: [BDA: Bangla Text Data Augmentation Framework](https://arxiv.org/abs/2412.08753)
- Research description: Combines synonym replacement, random swap, back-translation, and paraphrasing with a semantic filtering step, reaching near full-data performance from significantly less labelled Bangla text.

#### Misinformation & harmful content

Two sides of the same problem: text that incites harm, and text that misleads. Both are studied mostly in English, and both behave differently once you leave it.

- Related work: [Same Claim, Different Judgment: Benchmarking Scenario-Induced Bias in Multilingual Financial Misinformation Detection](https://arxiv.org/abs/2601.05403)
- Research description: MFMD-Scen tests whether LLMs judge the same financial claim differently depending on who is asking. Across 22 models and four languages, injecting financial personas, regional contexts, and cultural identities consistently shifts verdicts, with bias amplified in low-resource languages and smaller models.
- Related work: [Violence Inciting Text Detection in Informal Bangla](https://aclanthology.org/2023.banglalp-1.26/)
- Research description: The shared task side of the FastText embedding work: classifying violence-inciting Bangla social media text under real-world, noisy, code-mixed conditions.

#### Accessibility & sign language

Sign languages are low-resource twice over: little data, and little attention. My work here targets instruction generation, so that learners of Bangla Sign Language get usable written guidance for producing a sign.

- Related work: [Prompting with Sign Parameters for Low-resource Sign Language Instruction Generation](https://openreview.net/forum?id=KkVMBkjbra)
- Research description: A prompting method that conditions on sign-language parameters — handshape, orientation, location, movement — to generate instructions for low-resource sign language education, released with the BdSLIG dataset. CV4A11y workshop at ICCV 2025.

#### LLM evaluation & bias

Benchmarks decide what the field optimizes for. I am interested in benchmarks that hold the claim fixed and vary the context around it, because that is where model judgment quietly breaks.

- Related work: [MFMD-Scen: Scenario-Induced Bias Across 22 Models and 4 Languages](https://arxiv.org/abs/2601.05403)
- Research description: English, Chinese, Greek, and Bengali, evaluated under role, region, personality, and identity scenarios. The gap between a model's verdict on a claim and its verdict on the same claim with a persona attached is the measurement.
- Related work: [Zero-shot Evaluation for Sign Language Instruction Generation](https://openreview.net/forum?id=KkVMBkjbra)
- Research description: How well do general-purpose vision-language models describe a sign they have never been trained on? BdSLIG provides the evaluation setting.

Related-work headings above sometimes describe a particular aspect of a paper. The publication records below provide the formal titles; repeated links identify the same work, not additional publications.

### Mentors and collaborators

I work within the [Systems and Software Lab (SSL)](https://cse.iutoic-dhaka.edu/ssl) in the Department of Computer Science and Engineering at the Islamic University of Technology. The people below are the mentors and collaborators I have written papers with.

- Hasan Mahmud: Graduate supervisor
- Profile: https://cse.iutoic-dhaka.edu/profile/hasan/education
- Mohsinul Kabir: Undergraduate thesis supervisor
- Profile: https://cse.iutoic-dhaka.edu/profile/mohsinul/education
- Md. Tariquzzaman: Junior Lecturer · M.Sc. student
- Md Kamrul Hasan: SSL faculty · co-author
- Md Farhan Ishmam: Collaborator
- Saiyma Sittul Muna: Collaborator

### Collaboration interests

I am always glad to collaborate on Bangla and low-resource language resources, accessibility technology, and multilingual evaluation. Interested in working together? Reach out: [tariquzzaman@iut-dhaka.edu](mailto:tariquzzaman@iut-dhaka.edu).

### Professional record

#### Appointments

##### Junior Lecturer, Computer Science & Engineering

- Date / term: Sep 2024 – Present
- Organization: [Islamic University of Technology](https://www.iutoic-dhaka.edu/)
- Details: Gazipur, Bangladesh. Member of the [Systems and Software Lab (SSL)](https://cse.iutoic-dhaka.edu/ssl). [Department profile](https://cse.iutoic-dhaka.edu/profile/tariquzzaman/education).


#### Education

##### M.Sc. in Computer Science & Engineering

- Date / term: Sep 2024 – Present
- Organization: [Islamic University of Technology](https://www.iutoic-dhaka.edu/)
- Details: Supervisor: [Hasan Mahmud](https://cse.iutoic-dhaka.edu/profile/hasan/education). Gazipur, Bangladesh.

##### B.Sc. in Computer Science & Engineering

- Date / term: Jan 2020 – Jun 2024
- Organization: [Islamic University of Technology](https://www.iutoic-dhaka.edu/)
- Details: Undergraduate thesis supervised by [Mohsinul Kabir](https://cse.iutoic-dhaka.edu/profile/mohsinul/education). Gazipur, Bangladesh.

##### Higher Secondary Certificate (HSC)

- Date / term: Jul 2017 – Jul 2019
- Organization: [Govt. City College, Chattogram](https://gccc.edu.bd/)

##### Secondary School Certificate (SSC)

- Date / term: Jan 2007 – Jun 2017
- Organization: [Saint Placid's School and College](https://stplacid.edu.bd/)


#### Honors & awards

##### Best Shared Task Paper Award

- Date / term: Dec 2023
- Organization: 1st Workshop on Bangla Language Processing (BLP) at EMNLP 2023
- Details: For [A Novel Informal Bangla FastText Embedding for Violence Inciting Text Detection](https://aclanthology.org/2023.banglalp-1.26/).


#### Teaching

Courses taught at the Islamic University of Technology; semesters are in brackets.

- CSE 4271 Computer Programming [Summer 2024–2025; Summer 2023–2024]
- CSE 4272 Computer Programming Lab [Summer 2024–2025; Summer 2023–2024]
- CSE 4404 Software Project Lab II (Supervisor) [Summer 2024–2025; Summer 2023–2024]
- CSE 4600 Design Project (Co-Supervisor) [Summer 2024–2025]
- CSE 4307 Database Management Systems [Winter 2024–2025]
- CSE 4308 Database Management Systems Lab [Winter 2024–2025; Winter 2023–2024]
- CSE 4593 Software Engineering [Winter 2024–2025]
- SWE 4304 Software Project Lab I (Supervisor) [Winter 2024–2025]
- SWE 4800 Thesis (Co-Supervisor) [Summer 2023–2024]
- CSE 4508 Relational Database Management Systems Lab [Winter 2023–2024]

#### Research experience

##### Graduate Researcher, Systems and Software Lab

- Date / term: Sep 2024 – Present
- Organization: [SSL, Islamic University of Technology](https://cse.iutoic-dhaka.edu/ssl)
- Details: Sign language instruction generation for Bangla Sign Language, and multilingual benchmarking of scenario-induced bias in large language models.

##### Undergraduate Thesis Researcher

- Date / term: 2023 – Jun 2024
- Organization: [SSL, Islamic University of Technology](https://cse.iutoic-dhaka.edu/ssl)
- Details: Informal Bangla FastText embeddings, violence-inciting text detection, and the BDA text augmentation framework.


#### Industry

##### Machine Learning Intern

- Date / term: May 2023 – Sep 2023
- Organization: [RedDot Digital Ltd.](https://www.reddotdigitalit.com/)
- Details: Dhaka, Bangladesh.


#### Skills

Areas I work in day to day, in research and in the classroom.

- Natural language processing: word embeddings, text classification, data augmentation, prompting and zero-shot evaluation
- Low-resource language processing, with a focus on Bangla and informal / code-mixed text
- Large language model evaluation, benchmark design, and bias analysis
- Accessibility technology and sign language datasets
- Teaching: computer programming, database management systems, software engineering, and project supervision

### Additional experience descriptions

These descriptions preserve context provided separately in the research content; they do not represent additional appointments.

#### Junior Lecturer, Computer Science & Engineering

- Date / term: Sep 2024 – Present
- Organization / context: [Islamic University of Technology](https://www.iutoic-dhaka.edu/) · Gazipur, Bangladesh
- Details: Teaching programming, databases, and software engineering, and supervising software project and design courses. See [teaching](cv.html#teaching) for the full course list.

#### Graduate Researcher, Systems and Software Lab

- Date / term: Sep 2024 – Present
- Organization / context: [SSL, Islamic University of Technology](https://cse.iutoic-dhaka.edu/ssl) · M.Sc. in CSE
- Details: Supervisor: [Hasan Mahmud](https://cse.iutoic-dhaka.edu/profile/hasan/education). Sign language instruction generation and multilingual LLM evaluation.

#### Undergraduate Thesis, Systems and Software Lab

- Date / term: 2023 – Jun 2024
- Organization / context: [SSL, Islamic University of Technology](https://cse.iutoic-dhaka.edu/ssl) · B.Sc. in CSE
- Details: Supervisor: [Mohsinul Kabir](https://cse.iutoic-dhaka.edu/profile/mohsinul/education). Informal Bangla embeddings, violence-inciting text detection, and Bangla text augmentation.

#### Machine Learning Intern

- Date / term: May 2023 – Sep 2023
- Organization / context: [RedDot Digital Ltd.](https://www.reddotdigitalit.com/) · Dhaka, Bangladesh

### Publications

Author names and order are reproduced exactly as recorded. Publication type, venue, and year are retained without inferring a newer status.

#### Same Claim, Different Judgment: Benchmarking Scenario-Induced Bias in Multilingual Financial Misinformation Detection

- Authors: Zhiwei Liu; Yupen Cao; Yuechen Jiang; Mohsinul Kabir; Polydoros Giannouris; Chen Xu; Ziyang Xu; Tianlei Zhu; Md. Tariquzzaman; Triantafillos Papadopoulos; Yan Wang; Lingfei Qian; Xueqing Peng; Zhuohan Xie; Ye Yuan; Saeed Almheiri; Abdulrazzaq Alnajjar; Mingbin Chen; Harry Stuart; Paul Thompson; Prayag Tiwari; Alejandro Lopez-Lira; Xue Liu; Jimin Huang; Sophia Ananiadou
- Year: 2026
- Type: conference
- Venue: Findings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)
- Venue website: https://2026.aclweb.org/
- Research areas: LLM Evaluation; Misinformation
- Primary URL: https://arxiv.org/abs/2601.05403
- Paper: https://arxiv.org/abs/2601.05403

#### Prompting with Sign Parameters for Low-resource Sign Language Instruction Generation

- Authors: Md. Tariquzzaman; Md Farhan Ishmam; Saiyma Sittul Muna; Md Kamrul Hasan; Hasan Mahmud
- Year: 2025
- Type: workshop
- Venue: 4th Workshop on Computer Vision for Accessibility (CV4A11y) at ICCV 2025
- Venue website: https://cv4a11y.github.io/ICCV2025/index.html
- Research areas: Accessibility; Bangla NLP
- Primary URL: https://openreview.net/forum?id=KkVMBkjbra
- Paper: https://openreview.net/forum?id=KkVMBkjbra
- Code: https://github.com/tariquzzamanf/SPIP
- Dataset: https://huggingface.co/datasets/aplycaebous/BdSLIG
- Video: https://drive.google.com/file/d/10QgGeiHcLzH5HIqXrYUBx6rw_9PpZMZk/view

#### A Novel Informal Bangla FastText Embedding for Violence Inciting Text Detection

- Authors: Md. Tariquzzaman; Md. Wasif Kader; Audwit Nafi Anam; Naimul Haque; Mohsinul Kabir; Hasan Mahmud; Md Kamrul Hasan
- Year: 2023
- Type: workshop
- Venue: 1st Workshop on Bangla Language Processing (BLP) at EMNLP 2023
- Venue website: https://blp-workshop.github.io/2023/
- Award: Best Shared Task Paper Award
- Research areas: Harmful Content; Bangla NLP
- Primary URL: https://aclanthology.org/2023.banglalp-1.26/
- Paper: https://aclanthology.org/2023.banglalp-1.26/
- Code: https://github.com/tariquzzamanf/VITD
- Dataset: https://github.com/blp-workshop/blp_task1
- Video: https://aclanthology.org/2023.banglalp-1.26.mp4

#### BDA: Bangla Text Data Augmentation Framework

- Authors: Md. Tariquzzaman; Audwit Nafi Anam; Naimul Haque; Mohsinul Kabir; Hasan Mahmud; Md Kamrul Hasan
- Year: 2024
- Type: preprint
- Venue: arXiv preprint arXiv:2412.08753 (2024)
- Research areas: Text Augmentation; Bangla NLP
- Primary URL: https://arxiv.org/abs/2412.08753
- Paper: https://arxiv.org/abs/2412.08753

### Code and datasets

#### BdSLIG

- Date / term: 2025
- Organization / context: Bangla Sign Language instruction generation dataset
- Details: Released on Hugging Face alongside the CV4A11y @ ICCV 2025 paper.
- Dataset: https://huggingface.co/datasets/aplycaebous/BdSLIG

#### SPIP

- Date / term: 2025
- Organization / context: Sign Parameter Informed Prompting
- Details: Reference implementation for prompting with sign parameters.
- Code: https://github.com/tariquzzamanf/SPIP

#### VITD

- Date / term: 2023
- Organization / context: Violence Inciting Text Detection
- Details: Informal Bangla FastText embedding and BiLSTM classifier from the BLP 2023 shared task.
- Code: https://github.com/tariquzzamanf/VITD

### Recorded output counts

Snapshot counts from the source; recalculate when the publication record changes.

- Publications: 4
- Peer-reviewed: 3
- Best paper award: 1
- Code &amp; data releases: 3

### Historical news inventory (not displayed on the homepage)

- Mar 2026: [Same Claim, Different Judgment](https://arxiv.org/abs/2601.05403) accepted to Findings of ACL 2026.
- Oct 2025: [Prompting with Sign Parameters](https://openreview.net/forum?id=KkVMBkjbra) accepted at the [CV4A11y](https://cv4a11y.github.io/ICCV2025/index.html) workshop at ICCV 2025.
- Dec 2024: [BDA: Bangla Text Data Augmentation Framework](https://arxiv.org/abs/2412.08753) released on arXiv.
- Sep 2024: Joined [IUT](https://www.iutoic-dhaka.edu/) as a Junior Lecturer in CSE and started my M.Sc. in CSE.
- Jun 2024: Completed my B.Sc. in CSE at [IUT](https://www.iutoic-dhaka.edu/).
- Dec 2023: [A Novel Informal Bangla FastText Embedding](https://aclanthology.org/2023.banglalp-1.26/) received the Best Shared Task Paper Award at [BLP @ EMNLP 2023](https://blp-workshop.github.io/2023/).

### Personal interests — owner-supplied favorites

- Anime (ranked): Attack on Titan; Monster; Death Note; Naruto; Dragon Ball Z; One Piece; Jujutsu Kaisen; Tokyo Ghoul; Ace of Diamond; Fullmetal Alchemist.
- Movies (ranked favorites, not a complete watch history): Fight Club; The Matrix; Interstellar; Avengers: Infinity War; Spider-Man: Into the Spider-Verse; Coherence; Your Name; Gone Girl.
- Books: Meditations by Marcus Aurelius.
- Sports: Bayern Munich.
- Preserve this order and do not infer further preferences. Titles use standard spelling. The book cover is illustrative; no particular edition was specified.

### Existing page metadata and addresses

Text and addresses retained for continuity and search metadata. These do not prescribe the new design or require the same wording.

#### Index

- Title: Md. Tariquzzaman - CSE Lecturer and NLP Researcher at IUT
- Description: Official academic website of Md. Tariquzzaman, Junior Lecturer in Computer Science and Engineering at Islamic University of Technology (IUT), with research in NLP, Bangla NLP, misinformation detection, sign language instruction generation, and LLM evaluation.
- Canonical: https://tariquzzamanf.github.io/

#### Research

- Title: Research by Md. Tariquzzaman - NLP, Bangla NLP, LLM Evaluation
- Description: Research by Md. Tariquzzaman, CSE Junior Lecturer at Islamic University of Technology (IUT), covering NLP, Bangla NLP, misinformation detection, sign language instruction generation, text augmentation, and LLM evaluation.
- Canonical: https://tariquzzamanf.github.io/research.html

#### Publications

- Title: Publications · Md. Tariquzzaman
- Description: Peer-reviewed publications and preprints by Md. Tariquzzaman on Bangla NLP, misinformation detection, sign language instruction generation, text augmentation, and LLM evaluation.
- Canonical: https://tariquzzamanf.github.io/publications.html

#### Cv

- Title: Curriculum Vitae - Md. Tariquzzaman, CSE Lecturer and NLP Researcher
- Description: Curriculum vitae of Md. Tariquzzaman, Junior Lecturer in Computer Science and Engineering at Islamic University of Technology (IUT), focused on NLP, Bangla NLP, and LLM evaluation.
- Canonical: https://tariquzzamanf.github.io/cv.html

#### Personal

- Title: Personal · Md. Tariquzzaman
- Description: A few things about Md. Tariquzzaman that the CV does not cover: anime, movies, books, and sports.
- Canonical: https://tariquzzamanf.github.io/personal.html

### Documents and image assets

These paths refer to assets in the current project. Keep the source CV and assets alongside this document.

- CV PDF: files/cv/tariq.pdf
- Profile image: profile.jpg
- Social image description: Md. Tariquzzaman, Junior Lecturer in Computer Science and Engineering at IUT
- Islamic University of Technology logo: logos/iut.jpg
- RedDot Digital Ltd. logo: logos/reddot.png
- Govt. City College, Chattogram logo: logos/gccc.png
- Saint Placid's School and College logo: logos/splacid.png

### Content notes for the rebuild

Teaching terms are preserved exactly, including Winter 2023–2024 and Summer 2023–2024; the appointment is separately recorded as beginning in September 2024. The source does not explain how those academic terms align with that start date. Do not silently alter either record.

No personal-page placeholders, icon names, CSS classes, color mappings, component settings, or interaction code are included. Internal links in preserved prose refer to the old site and should be mapped to the appropriate destination in the new site.
