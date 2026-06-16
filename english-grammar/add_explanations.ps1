$filePath = "C:\Users\hp\academics\english-grammar\index.html"
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

$explanations = @{
    # Chapter 1 - Noun
    'q1_1' = '"The news" → singular uncountable noun, তাই ''is'' হবে। News দেখতে plural মনে হলেও এটি singular।'
    'q1_2' = '"Cattle" একটি collective noun যা সর্বদা plural হিসেবে গণ্য হয়।'
    'q1_3' = '"Mouse" এর plural "mice"। এটি irregular plural নিয়মে পড়ে।'
    'q1_4' = '"Mathematics" দেখতে plural মনে হলেও এটি singular (বিজ্ঞানের নাম), তাই ''has'' হবে।'
    'q1_5' = '"Furniture" uncountable noun, এর কোনো plural form নেই।'
    'q1_6' = '"Scenery" uncountable noun, singular verb ''is'' নেয়।'
    'q1_7' = '"The police" সর্বদা plural verb নেয়। Collective noun হিসেবে plural।'
    'q1_8' = '"Scissors" সর্বদা plural (দুই অংশ নিয়ে গঠিত), তাই ''are'' হবে।'
    'q1_9' = '"The committee" collective noun → singular verb ''is'' (US English)।'
    'q1_10' = '"Advice" uncountable noun, singular verb ''is'' নেয়। ''Advices'' হয় না।'
    'q1_11' = '"Knowledge" uncountable noun, singular verb ''is'' নেয়।'
    'q1_12' = '"The United Nations" একটি organization → singular verb ''is'' হবে।'
    'q1_13' = '"The poor" = poor people (plural), তাই ''are'' হবে।'
    'q1_14' = '"Ten miles" দূরত্ব বোঝালেও এটি একটি single unit → singular verb ''is''।'
    'q1_15' = '"Everyone" indefinite pronoun → singular verb ''is'' নেয়।'

    # Chapter 2 - Pronoun
    'q2_1' = 'Object pronoun প্রয়োজন। ''I saw him'' → ''him'' হল object form।'
    'q2_2' = 'Possessive adjective ''my'' noun-এর আগে বসে। ''This is my book.'''
    'q2_3' = '''Who'' subject form, ''whom'' object form। ''Who came?'' → subject position।'
    'q2_4' = '''Whose'' possession বোঝায়। ''Whose pen is this?'' = কার কলম?'
    'q2_5' = 'Reflexive pronoun: I → myself, you → yourself/yourselves, he → himself।'
    'q2_6' = 'Indefinite pronoun ''something'' positive sentence-এ ব্যবহৃত হয়।'
    'q2_7' = '''Either'' → singular, দুটির মধ্যে একটি বোঝায়। ''Either of the two'' + singular verb।'
    'q2_8' = '''Which'' নির্দিষ্ট সংখ্যক বিকল্পের মধ্যে থেকে বেছে নেয়।'
    'q2_9' = 'Object pronoun ''him'' → ''I saw him yesterday.'''
    'q2_10' = '''Who'' subject form → ''The man who came...'' (who = subject of ''came'')'
    'q2_11' = '''Neither...nor'' → correlated conjunction pair।'
    'q2_12' = '''Where'' place বোঝায়। ''The house where I was born.'''
    'q2_13' = '''Myself'' reflexive, কিন্তু verb ''did'' লাগবে। ''I myself did the work.'''
    'q2_14' = '''They enjoyed themselves'' → plural reflexive pronoun।'
    'q2_15' = 'Question-এ ''anything'' ব্যবহৃত হয়। ''Is there anything...?'''

    # Chapter 3 - Adjective
    'q3_1' = '''Honest'' vowel sound দিয়ে শুরু, তাই ''an'' হবে। (h silent)'
    'q3_2' = '''Than'' comparative degree নির্দেশ করে, তাই ''better'' হবে।'
    'q3_3' = '''The'' + superlative ''tallest'' → ''the tallest girl'''
    'q3_4' = '''Ever seen'' → superlative degree ''best'' হবে।'
    'q3_5' = '''Than'' থাকায় comparative ''taller'' হবে (short adjective)।'
    'q3_6' = 'Positive degree: ''kind'' এখানে adjective হিসেবে ব্যবহৃত হয়েছে।'
    'q3_7' = '''Than'' থাকায় comparative ''more intelligent'' হবে (long adjective)।'
    'q3_8' = '''Of the two'' → ''the + comparative'' structure: ''the better''।'
    'q3_9' = '''Bad'' এর irregular comparative ''worse''।'
    'q3_10' = '''Beautiful'' একটি Descriptive adjective (বর্ণনামূলক বিশেষণ)।'
    'q3_11' = '''Which'' interrogative adjective হিসেবে option বোঝাতে ব্যবহৃত হয়।'
    'q3_12' = '''The'' demonstrative adjective হিসেবে নির্দিষ্ট অর্থে ব্যবহৃত হয়।'

    # Chapter 4 - Verb
    'q4_1' = '''He'' singular subject → ''goes'' (Present tense, third person)। এখানে ''going'' হবে না কারণ auxiliary verb ''is'' নেই।'
    'q4_2' = '''Has'' + past participle → ''written'' (irregular verb)। Write-wrote-written।'
    'q4_3' = '''Swimming'' এখানে subject-এর কাজ করছে, তাই এটি Gerund (noun as verb+ing)।'
    'q4_4' = 'Modal ''must'' → bare infinitive ''do''। Modal + V1।'
    'q4_5' = '''The ring made hand'' → past participle ''made'' (non-finite)।'
    'q4_6' = '''Enjoy'' → gerund takes: ''enjoy reading''।'
    'q4_7' = '''Ought to'' → সবসময় to-infinitive নেয়: ''ought to respect''।'
    'q4_8' = '''The sleeping boy'' → present participle ''sleeping'' adjective হিসেবে কাজ করছে।'
    'q4_9' = '''Before dinner yesterday'' → past perfect ''had finished'' (past of past)।'
    'q4_10' = '''Let'' → bare infinitive: ''let me go''।'

    # Chapter 5 - Adverb
    'q5_1' = 'Adverb ''fluently'' verb ''speaks'' কে modify করছে। Adjective না হয়ে adverb বসে।'
    'q5_2' = '''So...that'' structure: ''so fast that'' = এত দ্রুত যে (result বোঝায়)।'
    'q5_3' = '''Rarely'' একটি frequency adverb যা ''কদাচিৎ'' অর্থে ব্যবহৃত হয়।'
    'q5_4' = 'Manner adverb ''carefully'' verb ''drives'' কে modify করে।'
    'q5_5' = '''Too'' = অতিরিক্ত (negative meaning): ''too clever to be tricked''।'
    'q5_6' = '''Overdue'' = নির্ধারিত সময়ের পরে (late)। ''Hardly due'' বা ''hard due'' হয় না।'

    # Chapter 6 - Preposition
    'q6_1' = 'বছরের পূর্বে ''in'' বসে: ''in 1990''।'
    'q6_2' = 'দিনের নামের পূর্বে ''on'' বসে: ''on Monday''।'
    'q6_3' = 'নির্দিষ্ট সময়ের জন্য ''at'' বসে: ''at 3 o''clock''।'
    'q6_4' = 'বড় শহরের জন্য ''in'' বসে: ''in Dhaka''।'
    'q6_5' = '''Die of'' (disease): ''die of cancer''। ''Die from'' injury-র জন্য।'
    'q6_6' = '''Suffer from'' disease-র জন্য fixed preposition।'
    'q6_7' = '''Jump onto'' = উপরে লাফানো (movement + surface)।'
    'q6_8' = '''Good at'' skill বোঝাতে fixed collocation: ''good at mathematics''।'
    'q6_9' = '''Fond of'' → fixed preposition।'
    'q6_10' = '''Married to'' → fixed preposition।'
    'q6_11' = '''Interested in'' → fixed preposition।'
    'q6_12' = 'Duration বোঝাতে ''for'': ''for two hours''। ''Since'' point of time-এর জন্য।'
    'q6_13' = '''Good at'' → fixed collocation (skill): ''good at math''।'
    'q6_14' = '''Afraid of'' → fixed preposition: ''afraid of dogs''।'
    'q6_15' = '''Die of'' (disease): ''die of cancer''। রোগের জন্য ''of'' বসে।'
    'q6_16' = '''Proud of'' → fixed preposition: ''proud of my country''।'
    'q6_17' = '''Married to'' → fixed preposition: ''married to a doctor''।'
    'q6_18' = '''Punished for'' (crime/reason): ''punished for his crime''।'
    'q6_19' = '''Interested in'' → fixed preposition: ''interested in music''।'
    'q6_20' = '''Arrive at'' (small place): ''arrive at the airport''। ''Arrive in'' (large place)।'

    # Chapter 7 - Conjunction
    'q7_1' = '''But'' contrast বোঝায়: poor ↔ honest (বিরোধ)।'
    'q7_2' = '''Although'' = despite the fact that (contrast): tired ↔ kept working।'
    'q7_3' = '''Work hard and you will pass'' → imperative + and + result।'
    'q7_4' = '''Both...and'' → paired conjunction (a fool and a rogue - উভয়ই)।'
    'q7_5' = '''As...as'' → positive degree comparison (সমান বোঝায়)।'

    # Chapter 9 - Article
    'q9_1' = '''Honest'' vowel sound (''h'' silent) দিয়ে শুরু → ''an''।'
    'q9_2' = '''University'' consonant sound ''yu'' দিয়ে শুরু → ''a''।'
    'q9_3' = '''The sun'' → unique thing (অদ্বিতীয় বস্তু) তাই ''the''।'
    'q9_4' = 'সাধারণভাবে ''music'' → no article (uncountable, generic)।'
    'q9_5' = '''The piano'' → musical instrument-এর আগে ''the'' লাগে।'
    'q9_6' = '''An honest man'' → ''honest'' vowel sound দিয়ে শুরু।'
    'q9_7' = '''A one-eyed man'' → ''one'' উচ্চারণ ''wan'' (w sound) দিয়ে শুরু, তাই ''a''।'
    'q9_8' = '''A European'' → ''European'' ''yoo'' sound দিয়ে শুরু, তাই ''a''।'
    'q9_9' = '''The Ganges'' → river-এর নামের আগে ''the'' বসে।'
    'q9_10' = '''The sun'' → unique object, তাই ''the''।'

    # Chapter 10 - Tense
    'q10_1' = '''At 8 pm yesterday'' → নির্দিষ্ট অতীত সময়, তাই Simple Past ''had''।'
    'q10_2' = '''Before'' → Present Perfect ''have seen'' (অনির্দিষ্ট অতীত)।'
    'q10_3' = '''By next year, for 10 years'' → Future Perfect Continuous ''will have been working''।'
    'q10_4' = '''When I arrived'' → Past Continuous ''were cooking'' (interrupted past)।'
    'q10_5' = '''Since 2010'' → Present Perfect Continuous ''has been teaching''।'
    'q10_6' = '''Tomorrow'' → Simple Future ''will go''।'
    'q10_7' = '''When I arrived'' → Past Continuous ''were having'' (interrupted past)।'
    'q10_8' = '''Since 2015'' → Present Perfect Continuous ''has been living''।'
    'q10_9' = '''Before we reached'' → Past Perfect ''had left'' (past of past)।'
    'q10_10' = '''Already'' → Present Perfect ''have read''।'
    'q10_11' = '''Every day'' → Simple Present ''goes'' (third person -he/she/it)।'
    'q10_12' = '''For two hours when the bell rang'' → Past Perfect Continuous ''had been working''।'
    'q10_13' = '''By 5 pm tomorrow'' → Future Perfect ''will have ended''।'
    'q10_14' = '''Now'' → Present Continuous ''is raining''।'
    'q10_15' = '''I realized that...'' → Past Perfect ''had forgotten'' (prior action)।'
    'q10_16' = '''Every day'' → Simple Present ''arrives'' (third person singular)।'
    'q10_17' = '''Since our school days'' → Present Perfect ''have known''।'
    'q10_18' = '''Next year'' → Simple Future ''will build''।'
    'q10_19' = '''When he came'' → Past Continuous ''was sleeping'' (interrupted past)।'
    'q10_20' = '''By next June, for 10 years'' → Future Perfect ''will have worked''।'

    # Chapter 12 - S-V Agreement
    'q12_1' = '''News'' → singular verb ''is'' (looks plural but is singular)।'
    'q12_2' = '''Either...or'' → nearest subject ''I'' এর সাথে ''am'' হবে।'
    'q12_3' = '''The number of'' → singular verb ''is''।'
    'q12_4' = '''A number of'' → plural verb ''are''।'
    'q12_5' = '''Neither...nor'' → nearest subject ''students'' এর সাথে ''were''।'
    'q12_6' = '''Team'' (British English) → plural verb ''have'' possible (collective as individuals)।'

    # Chapter 13 - Voice
    'q13_1' = '''The cake was made by my mother'' → passive (past) = was + V3।'
    'q13_2' = '''English is spoken'' → passive (present) = is + V3।'
    'q13_3' = '''Is being written'' → passive continuous (present) = is + being + V3।'

    # Chapter 14 - Narration
    'q14_1' = '''I am busy'' → ''he was busy'' (present→past, I→he)।'
    'q14_2' = '''Will come tomorrow'' → ''would come the next day'' (will→would, tomorrow→the next day)।'
    'q14_3' = '''Please'' request বোঝায়, তাই ''requested'' হবে।'

    # Chapter 15 - Transformation
    'q15_1' = '''Being tired, he slept'' → একটি participle phrase, তাই Simple sentence।'
    'q15_2' = '''What an honest man he is!'' → exclamatory করতে ''what a/an + adjective + noun'' pattern।'
    'q15_3' = '''No other boy is as tall as he'' → positive degree (as...as pattern)।'

    # Chapter 16 - Conditionals
    'q16_1' = 'Second conditional: If + past ''were'' + would + V1।'
    'q16_2' = 'Third conditional (inverted): Had + subject + V3, would have + V3।'
    'q16_3' = 'First conditional: If + present ''rains'' + will + V1।'
    'q16_4' = 'Second conditional: ''If I were you'' → universal subjunctive ''were''।'
    'q16_5' = 'Third conditional: If + had + V3, would have + V3 (''passed'')।'
    'q16_6' = 'Inverted second conditional: ''Were I'' → ''I would fly''।'

    # Chapter 21 - Word Formation
    'q21_1' = '''Mis-'' prefix অর্থ ''wrong'' (ভুল): misunderstand, mislead।'
    'q21_2' = '''-tion'' suffix noun গঠন করে: education, decision, formation।'
    'q21_3' = '''Beauty'' → adjective ''beautiful'' (y → i + ful suffix)।'

    # Chapter 22 - Synonyms & Antonyms
    'q22_1' = '''Gorgeous'' → ''Beautiful'' -এর synonym (প্রতিশব্দ)।'
    'q22_2' = '''Poor'' → ''Rich'' -এর antonym (বিপরীত শব্দ)।'
    'q22_3' = '''Courageous'' → ''Brave'' -এর synonym (সাহসী)।'

    # Chapter 23 - Idioms & Phrases
    'q23_1' = '''Break the ice'' idiom-টির অর্থ ''প্রথম পদক্ষেপ নেওয়া'' বা আলাপ শুরু করা।'
    'q23_2' = '''Once in a blue moon'' অর্থ ''খুব কদাচিৎ'' (very rarely)।'
    'q23_3' = '''Piece of cake'' অর্থ ''সহজ কাজ'' (very easy task)।'
    'q23_4' = '''Under the weather'' অর্থ ''অসুস্থ'' (feeling ill)।'
    'q23_5' = '''Hit the nail on the head'' অর্থ ''সঠিক কথা বলা'' (to be exactly right)।'

    # Chapter 24 - Phrasal Verbs
    'q24_1' = '''Look after'' phrasal verb-টির অর্থ ''দেখভাল করা'' (take care of)।'
    'q24_2' = '''Give up'' অর্থ ''হার মানা'' বা ছেড়ে দেওয়া (surrender/quit)।'
    'q24_3' = '''Turn down'' অর্থ ''প্রত্যাখ্যান করা'' (reject/refuse)।'
    'q24_4' = '''Put off'' অর্থ ''মুলতুবি রাখা'' বা পিছিয়ে দেওয়া (postpone)।'

    # Chapter 25 - One Word Substitution
    'q25_1' = '''Bibliophile'' = book lover (যিনি বই ভালোবাসেন)।'
    'q25_2' = '''Democracy'' = people + government (গণতন্ত্র: জনগণের সরকার)।'
    'q25_3' = '''Misogynist'' = woman hater (যিনি নারী ঘৃণা করেন)।'
    'q25_4' = '''Regicide'' = killing of a king (রাজহত্যা)।'
    'q25_5' = '''Somnambulist'' = sleepwalker (যে ঘুমে হাঁটে)।'

    # Chapter 30 - BCS English
    'q30_1' = '''One of those who'' → who ''those'' -কে refer করে, তাই plural verb ''are'' হবে।'
    'q30_2' = 'Indirect speech-এ present tense past tense-এ পরিবর্তিত হয়: ''I am'' → ''he was''।'
    'q30_3' = '''The news'' singular uncountable noun, তাই singular verb ''is'' হবে।'
    'q30_4' = '''Deal in'' (ব্যবসা করা) পণ্যের জন্য ব্যবহৃত হয়। ''Deal with'' ব্যক্তি/সমস্যার জন্য।'
    'q30_5' = 'Direct → Indirect: ''can'' → ''could'', first person ''I'' → third person ''he''।'

    # Chapter 31 - University Admission
    'q31_1' = '''Prefer'' এর সাথে ''to'' preposition ব্যবহৃত হয়: ''prefer coffee to tea''।'
    'q31_2' = '''Diligent'' অর্থ পরিশ্রমী, এর synonym ''hardworking''।'
    'q31_3' = '''Danger'' → verb form ''endanger'' (বিপন্ন করা)।'

    # Chapter 32 - IELTS
    'q32_1' = 'Passive voice: ''is expected'' (The trend is expected to continue)।'
    'q32_2' = '''The number of'' → singular verb ''is'' (যদিও ''cars'' plural)।'
    'q32_3' = 'Band 7 = ''Good User'' — IELTS ব্যান্ড স্কেলে Band 7-কে Good User ধরা হয়।'
}

$count = 0
foreach ($key in $explanations.Keys) {
    $checkPattern = "<input[^>]*name=""$key""[^>]*>[\s\S]*?<div class=""feedback"">[^<]*</div>\s*<div class=""explanation"">"
    if ($content -match $checkPattern) {
        continue
    }

    $pattern = "(<input[^>]*name=""$key""[^>]*>[\s\S]*?<div class=""feedback"">[^<]*</div>)(\s*)(</div>)"
    $replacement = "`${1}`r`n<div class=""explanation"">$($explanations[$key])</div>`r`n`${3}"

    $newContent = $content -replace $pattern, $replacement
    if ($newContent -ne $content) {
        $content = $newContent
        $count++
    }
}

[System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
Write-Host "Added $count explanation divs"
