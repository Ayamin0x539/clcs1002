

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image black = "#000000"
image bg windowbg = "window.png"
image bg bed_day = "bedroomday.png"
image bg bed_night = "bedroomnight.png"
image bg house_day = "roomday.png"
image bg house_night = "roomnight.png"
image bg park = "park.jpg"
image bg park_day = "childrens_park_day.jpg"
image bg park_evening = "childrens_park_evening.jpg"
image bg park_night = "childrens_park_night.jpg"
image bg school_gate = "school_gate_2.jpg"
image bg cafeteria = "cafeteria.jpg"
image bg class_day = "Classroom_02_day.jpg"
image bg class_evening = "Classroom_02_evening.jpg"
image bg class_night = "Classroom_02_night.jpg"
image bg class_entrance_day = "Classroom_03_day.jpg"
image bg class_entrance_evening = "Classroom_03_evening.jpg"
image bg class_entrance_night = "Classroom_03_night.jpg"
image bg math_day = "classroom_morning.jpg"
image bg math_afternoon = "classroom_afternoon.jpg"
image bg math_evening = "classroom_evening.jpg"
image bg hallway = "hallwayday.png"
image bg hallway_night = "hallwaynight.png"
image bg corridor_morning = "school_corridor_morning.jpg"
image bg corridor_afternoon = "school_corridor_afternoon.jpg"
image bg corridor_night = "school_corridor_night.jpg"
image bg blackgrid = "gridworld.jpg"
image bg whitegrid = "gridworld-white.jpg"
image bg jazz = "jazz.jpg"
image bg courtroom = "courtroom.jpg"
image bg ginsberg = "ginsberg.jpg"
image bg train = "train.jpg"
image bg moloch = "moloch.jpg"
image bg shrew = "shrew.jpg"
image bg suicide = "suicide.jpg"
image bg nakedxxx = "nakedxxx.jpg"
image bg rockland = "rockland.jpg"
image bg molochgreen = "molochgreen.jpg"
image bg molochred = "molochred.jpg"
image bg sacrifice = "sacrifice.jpg"
image bg molochlight = "molochlight.jpg"
image bg buttons1 = "buttons1.png"
image bg buttons2 = "buttons2.png"
image bg buttons3 = "buttons3.png"
image bg buttons4 = "buttons4.png"
image bg buttons5 = "buttons5.png"


#Character images here.
image mom normal = "mom0001.png"
image mom surprised = "mom0002.png"
image aura normal = "aura0001.png" # made a bit smaller, for now.
image aura slight_surprise = "aura0002.png"
image aura enthusiastic = "aura0003.png"
image aura nervous = "aura0004.png"
image aura he = "aura0005.png"
image aura shock = "aura0006.png"
image aura happy = "aura0007.png"
image aura sleep = "aura0008.png"
image aura sleepy = "aura0009.png"
image aura concentrating = "aura0010.png"
image sumner normal = "sumner0001.png"
image sumner smile = "sumner0002.png"
image sumner glad = "sumner0003.png"
image sumner smile_nice = "sumner0004.png"
image sumner worried = "sumner0005.png"
image dylan normal = "dylan0001.png"
image dylan thinking = "dylan0002.png"
image dylan serious = "dylan0003.png"
image randall normal = "randall0001.png"
image randall sigh = "randall0002.png"
image randall glad = "randall0003.png"
#image aura surprised = ""
#image test small = "test0019.png" #the smaller one


# Music file shortcuts
# Character Themes
define music_aura = "Silver Blue Light.mp3" # Aura's theme.
define music_bed = "Music for Manatees.mp3" # played in house/bedroom
define music_dyl = "Sidewalk Shade.mp3" #Dylan's theme
define music_dyl_slow = "Sidewalk Shade - slower.mp3" #Dylan's theme, slowed
# General Themes
define music_light = "Carefree.mp3" # light, carefree music
define music_complex = "Lift Motif.mp3" # played when studying philosophies?
define music_day = "Summer Day.mp3" # daily music//music for walking around during the day
define music_night = "George Street Shuffle.mp3" # music for walking around at night
define music_class = "Infinite Perspective.mp3" # like Town, Flow of Time, People
define music_pondering = "On the Ground.mp3" # music for when MC is thinking.
define music_end = "Heartwarming.mp3" # credits theme, for now, I suppose.
define music_howl = "Gypsy Shoegazer.mp3" # music when Howl movie plays

# Declare characters used by this game.
define a = DynamicCharacter("aura_name", color="#f7a6fd", show_two_window=True) # light-pink #alt: ffcce5
define d = Character("Dylan", color="#0066cc", show_two_window=True) # dark-blue
define r = DynamicCharacter("mc_name", color="#c0c0c0", show_two_window=True) # grey
define ran = Character("Mr. Randall", color="#ff9933", show_two_window=True) # orange
define s = DynamicCharacter("sumner_name", color="#00ff80", show_two_window=True) # light green
define m = DynamicCharacter("mom_name", color="#9999ff", show_two_window=True) # off-purple-blue
define pb = Character("Passing Boy", color="#006666", show_two_window=True) # dark turqoise
define pg = Character("Passing Girl", color="#99004c", show_two_window=True) # maroon red
define p = Character("Presenter", color="#99004c", show_two_window=True) #presentation lady

# Various props.
image picasso = "picasso.jpg"
image plato = "plato.jpg"
image republic = "republic.jpg"
image aristotle = "aristotle.jpg"
image eric = "eric.jpg"
image akira = "akira.png"
image origami = "origami.png"

# The game starts here.
label start:
    ### debug
    #jump test_scene
    ### debug
    #jump week_6_2
    
    #Starting relationship values // POINT_AURA, POINT_DYLAN, POINT_SUMNER, and POINT_RANDALL.
    $ pt_a = 0 # points with aura
    $ pt_d = 0 # points with dylan
    $ pt_s = 0 # points with ms. sumner
    $ pt_r = 0 # points with mr. randall
    
    #Unknown names
    $ mc_name = "River"
    $ mom_name = "????"
    $ aura_name = "????"
    $ sumner_name = "????"
    
    #Switches
    $ q1 = False
    $ q2 = False

    scene black
    with dissolve
    
    # alarm clock here
    "I shut my alarm clock off and open my eyes."
    
    m "River!"
    
    "... River?"
    "That's not my name, is it?"
    
    menu:
        "No, that's not my name.":
            "I don't recall ever being called that."
            "This must be a dream."
            jump choose_name
        "Yes it is.":
            "Oh wait, yes it is."
            "That's right, after I was born, I was given that strange name."
            jump day_1

#If the player decides to choose the name, we will go here. This leads to scene day_1.
label choose_name:
    "That's right... my real name is..."
    
    # setting the player's name
    $ mc_name = renpy.input("What is your name? (Please type your name.)")
    
    "This must indeed a dream."
    "I should probably wake up..."
    r "Urgh..."
    "I groan as I turn in my bed."
    jump day_1
    
label day_1:
    m "Helloooooooo! Are you up?"
    "Who is that?"
    "... Oh right. That's my mom's voice."
    $ mom_name = "Mom"
    m "Are you up? School is going to start soon!"
    "I could hear her yelling at me down the stairs."
    r "I'm up!"
    "My voice cracked."
    "I must still be tired."
    "That's right..."
    "It was my first day of school."
    "My first day at Brightview High School."
    "I just wanted to go back to sleep..."
    m "I'm leaving for work!"
    m "You might want to start heading out soon!"
    r "Ugggghhhh..."
    "I groaned."
    "I knew my mom wouldn't be here to wake me up if I overslept."
    "She had always been busy with her day job, working long hours. Starting as early as possible and staying for overtime whenever she could."
    "She stayed for overtime pretty much everyday."
    "I began to mumble to myself."
    r "I need to get up..."
    "I open my eyes."
    scene bg bed_day
    with dissolve
    play music music_bed fadeout 1.0 fadein 1.0
    "I really don't want to go..."
    "I didn't want to meet new people."
    "I don't want to attend classes."
    "I don't want to learn about anything."
    "All I wanted to do was sleep."
    "I didn't really have any goals or anything..."
    "Why bother?"
    "Nevertheless, I got ready and headed downstairs."
    scene bg house_day
    with dissolve
    "Huh?"
    "I heard shuffling coming towards my direction."
    show mom surprised at right with moveinright
    m "Oh!"
    show mom normal at right
    with dissolve
    m "I didn't even notice, but I guess this year your school starts a bit earlier compared to last year."
    "Ah."
    "So I'll actually get to see my mom in the mornings."
    "At least for a little bit. That is, until..."
    m "I have to get going now. Enjoy your first day!"
    r "Yeah..."
    "Yeah right."
    # play sound door close
    hide mom
    "I stared at the door as my mom left for work."
    "I should probably start getting ready..."
    jump day_1_walk
    
label day_1_walk:
    scene bg park
    with fade
    play music music_day fadeout 1.0 fadein 1.0
    "I left my house and began on my way to school."
    "The path I took had a bunch of trees."
    "I looked to my right."
    scene bg park_day
    with slideleft
    r "Hmmm..."
    "I started mumbling to myself."
    r "What a beautiful park..."
    stop music
    a "Isn't it?"
    "...?!"
    "A quiet voice from my left."
    "I quickly turned."
    scene bg park
    with slideright
    "I looked around."
    show aura normal with dissolve
    play music music_aura
    "... and then saw someone."
    a "Hi!"
    r "Ummm..."
    menu:
        "Who is this person?"
        "Ask who she is.":
            r "Uhh... hi."
            r "What's your name?"
            $ pt_a += 1 # POINT_AURA max: 1
            jump day_1_asked
        "...":
            r "..."
            "I decide to say nothing."
            jump day_1_no_ask
    return

label day_1_asked: # didn't ask aura her name
    a "Ummmm..."
    show aura nervous with dissolve
    a "Uhhh...."
    "She chuckled nervously."
    "... did she forget her own name?"
    show aura enthusiastic with dissolve
    a "Oh!"
    a "My name is Aurelia!"
    a "But that's kind of hard to say, so you can just call me Aura."
    jump day_1_cont

label day_1_no_ask: # asked aura her name
    a "..."
    r "..."
    a "..."
    r "..."
    "The silence was unbearable."
    "I was about to say something, when..."
    show aura enthusiastic with dissolve
    a "Umm... Hi! My name's Aurelia! But since that's hard to say, you can just call me Aura!"
    jump day_1_cont
    
label day_1_cont:
    $ aura_name = "Aura"
    show aura normal with dissolve
    r "..."
    "What a strange name."
    #"This is bad."
    #"I haven't talked to anyone all summer."
    "After remaining silent for a while, I realized I should have responded with my name as well."
    r "I'm [mc_name]... N- n- nice to meet you?"
    "I stuttered."
    #"I was never good with speaking."
    #"I had public speaking anxiety issues ever since I was young."
    #"Forget public speaking. Most of time, I'm uncapable of even holding a conversation."
    #"That's why I stayed in my house all summer."
    #"It's not that I don't have friends."
    #"I just kept ignoring their invites."
    
    a "Nice to meet you too!"
    r "I..."
    "I struggled to say something."
    #"But what do I say after that?"
    #"I had always found that exchanging pleasantries were a waste of time, since they were typically meaningless."
    #"People greet each other every day, \"Good morning\", or \"How do you do\"..."
    #"But what does \"Good morning\" even mean? What if they're having a bad morning?"
    #"And does the asker of \"How do you do\" truly care about how that person is doing?"
    "But I was at a loss for words."
    a "...?"
    #"Lost in my thoughts, I completely forgot about the girl in front of me."
    #"Oh no. She must think I'm weird."
    "I pretended to notice something in the park on my right and looked away quickly."
    hide aura
    scene bg park_day
    with slideleft
    "..."
    "I pretended to focus my eyes on nothing in particular."
    "Mustering up my courage, I turned to look back at the girl."
    scene bg park
    with slideright
    "...?"
    "Huh?"
    "Where'd she go?"
    "I looked around."
    "... but the mysterious girl was no where to be found."
    "I continued onwards to school."
    jump day_1_school_morning
    
label day_1_school_morning:
    scene bg school_gate with dissolve
    play music music_day
    "I finally arrived at school."
    "I thought I saw Aura in the crowd of students walking into the building, but I wasn't sure if it was her."
    "Does she go to this school?"
    "She looked a bit too young to be a highschooler."
    "But the uniform she was wearing looks like the one the girls are wearing here."
    menu:
        "I..."
        "Wait a while longer.":
            $ pt_a += 1 # POINT_AURA max: 2
            "I waited..."
            "... and waited ..."
            "..."
            "......"
            "..........."
            "I started pacing."
            "..."
            r "This is getting me no where."
            "I decided to merge into the stream of students and enter the school."
        "Go inside.":
            "... Not wanting to think about it anymore, I merged into the stream of students and entered the school."
    scene bg hallway with dissolve
    "I tried to remember what classroom I was in."
    "I think it was 2A."
    "I walked down the hall of the second floor, looking for 2A."
    "I had just found it, when..."
    play music music_dyl
    show dylan normal at right with moveinright
    d "Yo."
    "Dylan."
    menu:
        "I..."
        "Respond.":
            $ pt_d += 1 # POINT_DYLAN max: 1
            r "Hey."
        "Say nothing.":
            r "..."
            d "Silent as always eh?"
            d "That's aight, you must be tired or somethin'."
    "Dylan was one of my only friends since elementary school."
    "I guess you could say he was a sort of trouble maker."
    "Always lazing about, never doing any work..."
    "But he was easy to talk to."
    d "What class number?"
    menu:
        "Lie and say 5B.":
            $ pt_d += 1 # POINT_DYLAN max: 2
            r "I'm in class 5B."
            d "..."
            "Dylan stared at me for a while."
            r "What?"
            d "Oh come on, I know you're in 2A!"
            r "... how?"
            d "I saw it on the paper in the bulletin board downstairs!"
            d "I was just wondering if you knew."
            r "Haha, you got me..."
            d "Hahahahaha!"
            "I remember when we would always joke around like this."
            "Those were the fun days."
        "Tell the truth.":
            r "I'm in class 2A."
            d "Really? No way! Me too!"
    r "It's right over there."
    "I pointed at the door with \"2A\" on a sign above it."
    show dylan thinking with dissolve
    d "Aight, let's go in!"
    "We walked into the class."
    hide dylan
    scene bg class_entrance_day with dissolve
    play music music_class
    "There were only a few students in the room."
    "So we weren't late."
    "I followed Dylan."
    "He took a seat in the back... as always."
    "I joined him."
    scene bg class_day with dissolve
    "Not a bad view."
    show dylan normal at right with moveinright
    d "I wonder who our teacher is."
    r "Hmm..."
    "The room began to fill up quickly."
    d "..."
    r "..."
    d "So over the summer, I built this neat boat out of cardboard."
    r "..."
    d "I tested it out in the lake behind my house and..."
    r "..."
    d " ... so then I went back to the shop, and they said ..."
    "I think Dylan was saying something, but I tuned him out."
    "He liked to talk a lot, and usually about stuff that didn't matter."
    "I don't even think he knows that I'm not listening to him."
    "I don't even think he cares."
    show dylan thinking with dissolve
    d "... but there was so much paint! I tried to ..."
    "..."
    "After a while, someone came through the door and stood at the podium at the front of the class."
    "Dylan stopped talking and directed his attention to what appeared to be the teacher."
    hide dylan with moveoutright
    "Everyone was looking at the teacher now."
    "I squinted my eyes, since I couldn't really see that well from the back."
    show sumner normal with dissolve
    s "Hello students."
    s "My name is Ms. Sumner. I will be your teacher in the mornings."
    $ sumner_name = "Ms. Sumner"
    s "I look forward to working with you all."
    "There was chatter amongst the students in the room."
    s "Why don't we all start by introducing ourselves?"
    s "Starting from the front, say your name and one of your hobbies."
    "The students in the room one by one introduced themselves."
    "It finally came my turn."
    r "... My name is [mc_name]. I don't really have any hobbies."
    "..."
    "Everyone looked at me strangely."
    "I was the only one who didn't \"have any hobbies\"."
    "I was considering hiding under my desk."
    "Until..."
    show dylan normal at right with moveinright
    d "Hey, I'm Dylan. I like doing just whatever."
    hide dylan with moveoutright
    "..."
    "And with that, the attention of the class was shifted off of me."
    s "Now that everyone has introduced themselves, I will now introduce myself."
    show sumner smile with dissolve
    s "Like I said, I'm Ms. Sumner. My goal is to get you all to be creative, critical thinkers."
    s "You will have a class with me in the mornings, then break for lunch. Afterwards, you will have class with Mr. Randall in the afternoon."
    show sumner normal with dissolve
    s "Today's topic will be an introduction to the topic of this week: Aesthetics."
    s "We shall begin by showing a video."
    "Ms. Sumner set up a projector and began to play a video."
    "It was titled \"Aesthetics Philosophy of the Arts\"."
    "She stepped away from the center of the room as the video played."
    hide sumner with dissolve
    "How boring."
    "It was talking about \'aesthetics\'."
    "What IS aesthetics, anyways?"
    "Curious, I tuned in a little on the presentation."
    "... apparently, it's the philosophical study of beauty and art."
    "The presentation then showed a picture of Picasso's {i}Guernica{/i}."
    show picasso at truecenter with zoomin
    p "Is this portrait of brutal war ... beautiful?"
    "The presentation lady asked this question."
    "... how should I know?"
    "I thought it was just a mess of different objects scrambled together."
    "Ms. Sumner paused the video on the picture and interjected."
    show sumner normal at left with moveinleft
    s "This portrait shows the suffering of many living beings."
    s "It was one of the best anti-war paintings, and the message it conveyed was very powerful."
    hide sumner with moveoutleft
    "She began playing the video again."
    hide picasso with dissolve
    "..."
    "The picture was so abstract, I wouldn't have known that if Ms. Sumner hadn't told us."
    "The movie then moved on to talk about the philosopher Plato."
    "It talked about how triangles drawn in the sand were imperfect, and just a copy of the \'true essense of a triangle\', whatever that means."
    "I guess he thought that every object had a perfect form that didn't exist."
    "What was the point of having a perfect form if we couldn't see it though?"
    "According to Plato, ideas could only be grasped by reason, but one idea could be perceived through the senses..."
    "That idea was the idea of beauty."
    "I guess that has something to do with aesthetics."
    show plato at truecenter with zoomin
    "The movie then talked about the Symposium."
    "In the book, Plato argued that the manifestation of something beautiful attracts those who see it."
    p "He held a low opinion of artists and poets..."
    "... wasn't he a sort of artist and poet himself, though?"
    p "Plato did not write about aesthetics and art, but the \'idea of beauty\'."
    "I guess that makes some sort of sense."
    hide plato with dissolve
    "Plato was pretty interesting."
    show republic at truecenter with zoomin
    "The film then talked about the Republic."
    "In this one, Plato said that artists are actually copycats, or copiers of reality."
    "Apparently Plato mistrusted poets since they often spoke of things they can't truly know about."
    "... strange. According to this film, Plato spoke of ideals, and the ideal world."
    "Surely, Plato couldn't have \'truly known\' about these perfect objects he describes."
    "So shouldn't he mistrust himself as well?"
    "What a contradictory person."
    hide republic with dissolve
    "They followed the discussion of Plato with a discussion of another philosopher."
    "It was someone called \'Aristotle\'."
    "The name sounded familiar."
    show aristotle at truecenter with zoomin
    "He wrote a book on art theory called \'The Poetics\'."
    "Aristotle provided a rebuttal of Plato's critique of the arts."
    "Whereas Plato said poets just imitate, Aristotle argued that poets are artists."
    "Hmm..."
    menu: 
        "I think I agree with..."
        "Aristotle.":
            "Yeah. Aristotle makes more sense. Poets should be considered artists, not imitators."
        "Plato.":
            "Plato makes more sense. After all, poets are just copycats. They write so abstractly, and the ideas aren't even original most of the time."
    p "Aristotle focused more on tragedy than the idea of beauty though."
    "I thought it was pretty interesting how Aristotle outlined the details of his work in something called the rules of composition, comprised of 3 unities."
    p "The first unity of action represents a single action with no subplots, where each phase is a result of the previous."
    p "The second is time. Aristotle specified that the timeframe of a tragic event and the ensuing drama shouldn't exceed 24 hours."
    p "Finally, the last unity was place. The events should all take place in the same location."
    "Aristotle was a pretty meticulous guy."
    hide aristotle with dissolve
    "The movie then went through different time periods and the preceptions of aesthetics in all these periods."
    p "In the Rennaisance, there was a neo-classical view of aesthetics: symmetry, harmony, and order were important."
    p "In the 15th century, many thought that \'beauty\' was defined as harmony and perfection."
    p "In the 18th century, art was seen as an \'imitation of nature\'. There was a disengagement of practical concerns."
    "According to someone named Francis Hutchinson, humans have a natural sense of beauty and harmony, and the viewer of art must be knowledgeable and have refined senstibility."
    "I guess he was saying that only certain people can enjoy art."
    "Isn't that kind of unfair though?"
    "The film then moved to talk about the Enlightenment."
    p "People valued rationality over philosophy in this time period."
    p "Art and beauty are a middle ground between sensibility and reason."
    p "Sensibility and reason are brought together by the imagination."
    "I could see that."
    "The film then moved to talk about other people such as Hegel, Schopenhauer, and Dionysus, but I lost focus and started looking out the window."
    "It was a bit too long for my liking."
    "The end of the film caught my attention though."
    "It talked about how technology made works of art no longer unique and unrepeatable, in the sense that we could reprint, scan, and copy works of art."
    "We also had television that showed shows and movies multiple times. The re-airings of these works were obviously not unique."
    p "In summary, art may not have any practical purpose, but we relish and admire it nonetheless."
    "... and that concluded the video."
    show sumner normal at center with dissolve
    s "And that concludes the intro."
    s "For homework I would like you all to read \"The Two Cultures\" by C. P. Snow."
    s "That is all; you are all dismissed for lunch."
    hide sumner with moveoutleft
    "Ms. Sumner began gathering her papers, as the students began getting up and pouring out of the room."
    "I looked over to my right."
    show dylan thinking at right with moveinright
    play music music_dyl_slow
    "Dylan was fast asleep."
    d "..."
    r "Hey."
    d "...?"
    menu: 
        "I..."
        "Try to wake him up.":
            $ pt_d += 1 # POINT_DYLAN max: 3
            "I shook Dylan."
            r "Class is over."
        "Leave him alone for now.":
            "I think I'll leave him alone for now."
            "... I am kind of hungry though."
            "I waited."
            "And waited."
            "Eventually, all of the students in the classroom had left."
    d "Nnnn..."
    "He stirred."
    show dylan normal at right with dissolve
    d "Oh."
    "He finally woke up."
    d "Oh. Class is over."
    d "Lunch time?"
    menu:
        d "Wanna go check out the food in the cafeteria?"
        "Sure.":
            r "Yeah. Let's go."
        "Nah.":
            r "Nah, I'm not that hungry."
            "I lied."
            d "Well, come along anyways."
            "He began dragging me out of the room."
            "I guess I have no choice."
    hide dylan with dissolve
    "Dylan walked ahead."
    scene bg hallway with dissolve
    play music music_light
    "We left the classroom and walked out to the hall."
    "There was a huge crowd of students. I guess all of them were eager to go to lunch."
    "... and I had lost Dylan."
    "Where was the cafeteria anyways?"
    "..."
    "...?"
    "A flash of white caught my eye."
    show aura he at center with dissolve
    stop music
    "Is that...?"
    r "Hey!"
    show aura shock at center with dissolve
    "I started walking towards the girl."
    "But then another student walked through my line of sight."
    hide aura with dissolve
    "... she was gone."
    "I looked around, but couldn't find her anywhere."
    "..."
    "I continued downstairs to the cafeteria."
    scene bg cafeteria with dissolve
    "I looked around."
    "I finally found Dylan amongst the mass of students."
    show dylan normal at right with moveinright
    play music music_dyl_slow
    d "Yo."
    d "What took you so long?"
    $ mentioned_aura = False
    menu:
        "I..."
        "Mention the girl.":
            $ pt_a += 1 # POINT_AURA max: 3
            $ mentioned_aura = True
            r "Have you seen someone around here with white hair?"
            d "White hair? Like an old person?"
            r "No, like a young girl, about this tall."
            "I motioned with my hands to show roughly where her head was if she were standing up."
            show dylan thinking at right with dissolve
            d "Hmm..."
            d "..."
            r "..."
            show dylan normal at right with dissolve
            d "Nope, I can't say I know any girls with white hair."
        "Say I got lost.":
            r "I got lost."
            d "Hahahaha, me too!"
            r "..."
            r "Hahahaha."
            d "Ahahahahaha."
    r "We should probably get some food."
    d "Yeah, let's go."
    "We waited in line for what seemed forever."
    "After we got our trays, we sat down and ate."
    d "Wanna hang out today after school?"
    r "I'm not sure."
    r "We have that assignment to do."
    d "What assignment?"
    "Oh right, Dylan was probably asleep when Ms. Sumner mentioned it."
    $ correct_reading = True # tells whether we told Dylan the correct reading or not.
    menu:
        "Come to think of it... what was the assignment again?"
        "Read \"The Three Arts\" by B. C. Winter.":
            r "We have to read \"The Three Arts\" by B. C. Winter."
            d "Ah, gotcha."
            $ correct_reading = False
        "Read \"The Two Cultures\" by C. P. Snow.":
            r "We have to read \"The Two Cultures\" by C. P. Snow."
            d "Ah, gotcha."
    "We finished eating and headed upstairs to our next class."
    hide dylan with dissolve
    scene bg corridor_afternoon with dissolve
    play music music_day fadeout 1.0 fadein 1.0
    "This floor of the school looked a bit older than the one Ms. Sumner's class was on."
    "The light from the sun, now in the middle of the sky, shined through the windows."
    scene bg math_afternoon with dissolve
    "We walked into the room."
    "It looked like the students had already populated the room. We might have been a little late. We hurriedly took a seat in the back."
    show randall normal at center with dissolve
    ran "So..."
    ran "I'm Mr. Randall, your math and science teacher."
    ran "Everything that you've learned about mathematics..."
    show randall sigh at center with dissolve
    ran "I will redefine that this year."
    "Oh boy."
    show randall normal at center with dissolve
    "I knew I wouldn't be able to stand this guy."
    ran "First, we will take a look at the nature of the natural numbers."
    ran "We will denote the set of ..."
    "I quickly tuned him out."
    "I began to gaze out the window."
    "..."
    $ paid_attention = False
    menu:
        "I..."
        "Pay attention.":
            "I guess I'll try to put up with this guy for a bit."
            $ paid_attention = True
            ran "Natural numbers include 0, 1, 2, 3, etc."
            ran "A natural number cannot be a fraction."
            ran "It must be a whole number, so a number with non-zero decimal points cannot be a natural number."
            ran "Additionally, a natural number cannot be negative."
            ran "We will cover numbers other than natural numbers later."
            "..."
            "How boring."
            "That was enough for me."
            "I dozed off again."
        "Don't pay attention.":
            "I keep looking out the window and start daydreaming."
            "I think I fell asleep at one point."
    "..."
    "..."
    show randall sigh at center with dissolve
    ran "... such a number?"
    "I snapped awake."
    "I saw that Mr. Randall was making direct eye contact with me."
    r "I'm sorry, what?"
    ran "Is the number 3.42 a natural number?"
    if paid_attention:
        r "No. Natural numbers can't have non-zero decimal points..."
        "Woah."
        "I didn't think I'd have remembered that."
        show randall normal at center with dissolve
        ran "... Correct."
        "..."
        "He continued lecturing."
        "... I went back to sleep."
    else:
        menu:
            "The number 3.42... is it a natural number?"
            "I don't know.":
                r "I uh..."
            "I don't know.":
                r "I uh..."
            "I don't know.":
                r "I uh..."
        r "I really don't know."
        ran "..."
        ran "In the future, please try not to fall asleep in my class."
        "... Oh shoot."
        r "Got it..."
        show randall normal at center with dissolve
        "But it was so difficult."
        "I ended up dozing off again."
    "Good thing Mr. Randall didn't end up calling on me again until I woke up."
    "It was the bell that rang for the dismissal of school that woke me up."
    "I packed up my stuff and walked out into the hall."
    scene bg corridor_afternoon with dissolve
    play music music_night
    show dylan thinking at right with moveinright
    d "Not bad for a first day."
    r "Yeah."
    d "Catch ya tomorrow then."
    r "Yup."
    hide dylan with moveoutright
    "Dylan headed out of the school."
    menu:
        "I..."
        "Go to the hallway of Ms. Sumner's class.":
            $ pt_a += 1 # POINT_AURA max: 4
            "For some unexplainable reason, I wanted to check out that hallway again."
            scene bg hallway with dissolve
            "It was empty. All the students must have already left."
            "... I waited."
            "... and waited."
            "..."
            "After a while, I got bored."
            "I guess I should probably go home."
        "Go home.":
            "I have nothing else to do, so might as well go home."
    scene bg park_evening with dissolve
    "As I was walking home, I passed by the park."
    "... for some reason, I waited around for a while."
    "... but nothing interesting happened."
    "I continued home."
    scene bg house_day with dissolve
    "It was still pretty bright out."
    "I headed upstairs to my room."
    scene bg bed_day with dissolve
    play music music_bed fadeout 1.0 fadein 1.0
    "I should probably get started on that reading..."
    "I checked my notes."
    "\"The Two Cultures\" by C. P. Snow."
    if not correct_reading:
        "Oh."
        scene bg cafeteria with fade
        show dylan normal at right
        r "We have to read \"The Three Arts\" by B. C. Winter."
        d "Ah, gotcha."
        hide dylan
        scene bg bed_day with fade
        "... oops."
    "I opened the book of collections and found the article."
    "I began to read."
    "..."
    "......"
    r "Art and science are two cultures..."
    "..."
    r "Science is a culture in that it goes across all bounds, such as political and social standing..."
    r "Science even bridges people of different religions..."
    "I kept reading."
    r "Unscientific sentiments in artists lead to an \"anti-scientific\" misjudgment..."
    r "... use books for enjoyment rather than for learning..."
    r "... lack of understanding of scientists... using the terms \"refraction\" and \"polarized light\" incorrectly...."
    r "... couldn't tell what the 2nd law of thermodynamics was..."
    "I thought it was pretty interesting, actually."
    "Especially the part where the scientist side likened the question of whether someone knew the relationship between mass and acceleration to the question of \"Can you read?\""
    "I was getting tired though."
    "I flipped through a few more pages and then shut off the light."
    scene bg bed_night with dissolve
    "It was time to sleep."
    "..."
    "That wasn't too bad for a first day of school."
    "But no matter what, I couldn't get that mysterious person out of my head."
    "... I wonder if something interesting will happen tomorrow."
    "... I should go to sleep."
    scene black with dissolve
    stop music fadeout 1.0
    "..."
    jump day_2
    
label day_2:
    m "Are you up?"
    "I could hear my mom calling me from downstairs again."
    r "Nngh..."
    scene bg bed_day with dissolve
    play music music_bed
    "Morning already."
    "I got ready and headed down."
    scene bg house_day with dissolve
    "Again, my mom was about ready to leave for work."
    show mom normal at right with moveinright
    m "How was the first day?"
    r "It was alright."
    m "I see. I have to get going now, have a nice second day!"
    r "Yeah."
    hide mom with dissolve
    "And with that, she was gone."
    "... I should probably head out as well."
    scene bg park with dissolve
    "I began walking to school."
    "The same path."
    scene bg park_day with slideleft
    "The same park."
    scene bg park with slideright
    show aura normal
    "The same girl."
    stop music
    "Wait."
    show aura enthusiastic with dissolve
    play music music_aura
    a "HEY!"
    r "Ow!"
    "I jumped up in surprise."
    r "You shouldn't shout like that out of no where."
    show aura shock with dissolve
    a "Why not?"
    r "It scared me."
    show aura normal with dissolve
    a "Sorry."
    r "So who are you anyways?"
    a "I told you! I'm Aura!"
    r "I know that ..."
    r "... do you go to Brightview High?"
    a "What's that?"
    r "My high school."
    a "Never heard of it!"
    show aura happy with dissolve
    a "Ahahahahaha!"
    "... What a weird girl."
    "I kept walking."
    show aura normal at right with dissolve
    "Aura walked beside me."
    a "What's your favorite color?"
    "The question came from no where."
    r "Why?"
    a "Just tell me! What's your favorite color?"
    r "..."
    $ fav_color = "red"
    menu:
        "My favorite color is..."
        "Red.":
            r "It's red."
        "Green.":
            r "It's green."
            $ fav_color = "green"
        "Blue.":
            r "It's blue."
            $ fav_color = "blue"
        "Purple.":
            r "It's purple."
            $ fav_color = "purple"
        "Orange.":
            r "It's orange."
            $ fav_color = "orange"
        "Pink.":
            r "It's pink."
            $ fav_color = "pink"
        "Yellow.":
            r "It's yellow."
            $ fav_color = "yellow"
    a "Hmmmm..."
    show aura happy at right with dissolve
    a "I could see that."
    r "What do you mean?"
    show aura normal at right with dissolve
    a "You just seem like the type of person that would like the color [fav_color]."
    r "... I see..."
    "I didn't see at all."
    "What does she mean?"
    r "What about you?"
    r "What's your favorite color?"
    "I turned to look at Aura."
    hide aura with dissolve
    stop music
    "..."
    "But she wasn't there anymore."
    "... I could have sworn she was right there in my peripheral vision the whole time."
    "Strange."
    scene bg school_gate with dissolve
    play music music_day
    "Before I knew it, I was at the entrance to school."
    "I walked in."
    scene bg hallway with dissolve
    "I found class 2A much faster than I had yesterday."
    scene bg class_entrance_day with dissolve
    "I entered the classroom..."
    scene bg class_day with dissolve
    "... and sat in the back again."
    "Dylan wasn't here yet."
    show sumner normal at center with dissolve
    "Good morning class. Today, we -"
    show dylan normal at right with moveinright
    d "Sorry I'm late."
    "The whole class looked at him."
    s "Welcome. Please take a seat."
    "Ms. Sumner didn't look angry at all."
    d "Will do."
    "Dylan joined me in the back."
    hide dylan with moveoutright
    s "Today, we will be discussing the assigned C. P. Snow reading."
    if not correct_reading:
        d "Oh... I read the wrong article..."
        "Oops."
    s "Who can tell me the main focus of the article?"
    "Someone in the front raised their hand."
    "Classmate" "The main focus of the article is on the rift between scientists and artists."
    s "Correct. The article separates society into two cultures: those that are scientists, and those that are artists."
    s "Those of the \"traditional culture\", or artist, tend to chuckle with pity at the illiteracy of scientists."
    s "But on the other hand, no young scientist of any talent would feel that he isn't wanted, or that his work is ridiculous."
    "From what I remembered from the reading, both of the cultures seemed biased and full of themselves."
    s "Snow emphasizes that our school education is too specialised."
    s "He makes the argument that we should diversify our education."
    s "What do you guys think? Do we still have these categories today? And should we diversify more?"
    "Again, the person in the front row raised their hand."
    "Classmate" "I think that there are some people that are better in the arts than they are in the sciences, and vice versa..."
    "Classmate" "... but that shouldn't stop them from trying out the opposite discipline!"
    "I raised my hand."
    s "Yes, [mc_name]?"
    "... I didn't know what had gotten into me."
    "I usually never raise my hand."
    "But I felt strongly about this topic, for some reason."
    $ flag_both = False
    menu:
        "I believe that..."
        "Scientists are right.":
            r "I think science should receive priority in education though."
            r "Human would never progress without the advancements made possible by science."
        "Artists are right.":
            r "I think that they should teach art more often in schools."
            r "Freedom of expression is the most important thing anyone growing up could have."
        "Both are right.":
            r "I think that people should be well-versed in the literary arts as well as the scientific realm."
            $ flag_both = True
    s "Interesting points."
    if flag_both:
        "Snow believed that the two disciplines should be married as well."
    else:
        "On the contrary, Snow believed that the two disciplines should be married."
    s "That is enough for the discussion on Snow."
    s "We will now look at an opposing argument."
    "The class was handed a printed out article."
    "It was titled \"Aesthetics and the Two Cultures - Why Art and Science Should Be Allowed to Go Their Separate Ways\"."
    "Whoever this James Elkins guy was, he seemed like a pretty negative person."
    s "Please take a read through it."
    "Ms. Sumner retreated behind her desk to do some paperwork."
    hide sumner with moveoutleft
    "The whole class was silent."
    "Everyone was looking down at the paper."
    "Might as well take a look..."
    "..."
    "......"
    "From what I read, it seemed like Elkins' main argument was that there was no science in art."
    "He says hat art and science cannot be bridged by aesthetic discourse."
    "This guy must really be for the separation of the two cultures."
    "This article sounds more like a complaint, or a rant, than an actual argument."
    show sumner normal with dissolve
    s "As you can all see, there are those that believe that the two cultures should be separated as well."
    "We then moved on to read another article."
    "This one was by someone named Vilem Flusser." 
    "It was titled \"Habit: The True Aesthetic Criterion\"."
    hide sumner normal with moveoutleft
    "Again, Ms. Sumner retreated to her desk as we read."
    "..."
    "......"
    "This one was different from the previous two."
    "It seemed like this Flusser dude was making a direct link between physics and art."
    show sumner normal with dissolve
    "Ms. Sumner went to the front of the room again."
    s "In this article, Flusser talks about entropy."
    s "He describes art as creating something new, and thus increasing entropy in the world."
    s "Now, does anyone know what \"improbability\" Flusser refers to is?"
    "The person in front raised their hand again."
    "No surprise."
    s "... Yes?"
    "Classmate" "The \"improbability\" he refers to is actually entropy, or \"chaos\"."
    "Classmate" "But eventually this \"chaos\" turns into something we're used to."
    "Classmate" "This is similar to a closed system eventually attaining equilibrium... at the expense that the entropy and chaos is born elsewhere."
    "Classmate" "It's like a huge surprise, a big bang, a noise, or a blast that jolts us, but we eventually get used to it."
    "Classmate" "Getting used to it is making it a \"habit\", and then eventually it dies with a wimper."
    "Classmate" "This is all referring to art, of course. When we see it for the first time it's a shock, but then we just get used to it."
    "... That was one part I disagreed with."
    "I didn't think that if you enjoyed something only for the first time, then it would \"die with a whimper\" as Flusser put it."
    "Another way Flusser said the \"surprise\" could be induced was through \"terror\"."
    "If we take for example the dawn of fire, at first humans were scared of fire."
    "But then we creatively learned how to use it."
    "Yet even today, we can still be fascinated by the sight of fire. So I didn't think that art merely died out in that fashion."
    s "Very good."
    s "It is almost time to break for today, but before that, I would like to give you another assignment."
    s "Please write an essay on the following topic:"
    s "Reflect on Elkins' and Snow's articles, and explain how they are relevant in your daily lives."
    s "It will be due next week."
    s "That is all."
    hide sumner with dissolve
    "The students began to get up and leave."
    show dylan thinking at right with moveinright
    "... of course, Dylan would be asleep."
    "I decided to let him be."
    hide dylan with moveoutright
    "I decided to head down to the cafeteria for lunch."
    scene bg hallway with dissolve
    play music music_light
    "An essay on the second day of school..."
    "I was not looking forward to writing it."
    "Those two articles have nothing to do with my daily life at all."
    "I'm not an artist, and I'm definitely not a scientist."
    "How should I know how the two cultures should interact with each other?"
    "I brushed it off for now."
    scene bg cafeteria with dissolve
    "I got in line for food."
    "It was a long line, as always."
    "..."
    "After what seemed like forever, I finally got my meal and sat down."
    "I wonder if Dylan ever woke up."
    "He's probably still dead asleep in that classroom."
    "..."
    "I finished my lunch."
    "I should probably head up to math."
    scene bg corridor_afternoon with dissolve
    "I dragged myself up to the floor with Mr. Randall's class on it."
    "...?!"
    "I saw a dark figure slowly walk into the room."
    show dylan thinking at right with moveinright
    d "Hungry..."
    show dylan thinking at center with dissolve
    d "So hungry..."
    show dylan thinking at left with dissolve
    d "So, so hungry..."
    hide dylan with moveoutleft
    "..."
    "How scary."
    "Well, it was his fault for sleeping in class and missing lunch."
    "I followed him into the room."
    scene bg math_afternoon with dissolve
    "The class was pretty much full."
    "I should probably start leaving lunch a bit earlier."
    ran "Today we will be discussing basic algebra."
    "I knew this was going to be a long afternoon."
    "..."
    "Thankfully, Mr. Randall didn't call on me again like he did yesterday."
    "Then again, I didn't fall asleep this time."
    "The dismissal bell rang after what seemed like forever."
    scene bg corridor_afternoon with dissolve
    play music music_night fadeout 1.0 fadein 1.0
    show dylan normal at right with moveinright
    d "... See ya."
    r "Later. Get something to eat."
    show dylan thinking at right with dissolve
    d "I plan on it."
    hide dylan with moveoutright
    "I started to head home as well."
    scene bg school_gate with dissolve
    "I exited the school."
    scene bg park_evening with dissolve
    "And began walking back, passing the park again."
    "..."
    "I saw a figure on the slides."
    "There was a lot of white on it."
    show aura sleep with dissolve
    "..."
    "She was asleep."
    "I decided to wait around."
    "We had no assignments today, so I didn't have any other obligations."
    "... well, besides that essay."
    "But I'll put that off until later."
    "I still had to figure out who this person was."
    #CHOICE: wait for her to wake up or no? -- implement this if you have time.
    #We will write assuming you chose to wait. In future implementation, add 1 to aura point.
    "So I would wait for her to wake up."
    "..."
    "I waited."
    "... and waited."
    "...... and waited."
    "..."
    scene bg park_night with dissolve
    show aura sleep with dissolve
    "Eventually people stopped passing by the park."
    "Night had fallen before I knew it."
    a "Nn..."
    "Aura stirred."
    show aura sleepy with dissolve
    a "..."
    r "..."
    a "...?"
    r "Good morning."
    show aura shock with dissolve
    a "Good morning."
    a "Wait, it's not morning... How long have I been asleep for?"
    r "I have no clue."
    r "I was walking home from school and found you asleep here."
    show aura he with dissolve
    a "I see."
    show aura nervous with dissolve
    a "Eheheheheh... that's embarrassing."
    r "Hahahaha. You should probably get home."
    show aura normal with dissolve
    a "Yeah, good idea. You, too."
    r "Yup. Take care."
    show aura happy with dissolve
    a "See ya!"
    "I kept walking home."
    scene bg house_night with dissolve
    play music music_night fadeout 1.0 fadein 1.0
    "What a strange encounter."
    "I hadn't gotten home this late in a while."
    "..."
    "Looks like my mom is working overtime again."
    "I probably won't see her until the morning."
    "I started up the stairs."
    scene bg bed_day with dissolve
    "I started thinking about the essay."
    r "How the subject material of the two articles relate to my everyday life, huh..."
    "..."
    "I couldn't think of anything."
    "Well, there was enough time. No need to stress about it now."
    "I finished up some math homework Mr. Randall assigned."
    scene bg bed_night with dissolve
    "And then I turned off the light."
    "... and then drifted slowly to sleep."
    stop music fadeout 1.0
    "..."
    scene black with dissolve
    "......"
    jump day_3
    
label day_3:
    play music music_bed fadein 1.0
    "The next day."
    scene bg bed_day with dissolve
    "I woke up." 
    scene bg windowbg with dissolve
    "... and looked out my window."
    "... too bright."
    scene bg bed_day with dissolve
    "I got up and got ready."
    "I headed downstairs."
    scene bg house_day with dissolve
    "I didn't see my mom anywhere."
    "..."
    "I found a note on the table."
    "\"I had to leave for an important meeting early this morning. Have a wonderful day! Love, Mom.\""
    "I figured."
    "I started heading out."
    scene bg park with dissolve
    play music music_day fadeout 1.0 fadein 1.0
    "The same old path."
    "..."
    "I glanced at the park to my right, as always."
    scene bg park_day with slideleft
    "..."
    "No sign of Aura today."
    scene bg park with slideright
    "I wonder if she made it home okay."
    "Maybe I'll see her again at school."
    scene bg school_gate with dissolve
    "There were so many more students in high school than middle school."
    "Seeing the students flood into the gates reminded me of a colony of fish."
    scene bg hallway with dissolve
    "I headed to classroom 2A."
    scene bg class_entrance_day with dissolve
    play music music_class fadeout 1.0 fadein 1.0
    "..."
    "Looks like I'm early today."
    "There were no students in the classroom yet."
    "But Ms. Sumner was already here."
    show sumner normal at right with moveinright
    "She looked up from her desk at me."
    s "..."
    r "..."
    show sumner smile at right with dissolve
    s "Good morning."
    "Woah."
    "I don't think I've ever seen her smile before."
    r "G- good morning."
    "I stammered as I took my usual seat in the back."
    hide sumner with dissolve
    scene bg class_day with dissolve
    show sumner normal at left with dissolve
    "..."
    "How awkward."
    "It was just Ms. Sumner and I in the class room."
    "I made a mental note to never come to class this early ever again."
    "..."
    "Gradually, students came in one by one."
    "When it was time to start, Ms. Sumner went to the front of the class."
    show sumner normal at center with dissolve
    s "Good morning class."
    s "Now, today we will -"
    play music music_dyl
    show dylan normal at right with moveinright
    d "..."
    "Dylan had just walked in the class."
    d "... oops."
    "He quickly took a seat beside me."
    hide dylan with moveoutright
    play music music_class fadeout 1.0 fadein 1.0
    s "Anyways, today we will be watching a movie."
    s "You will then be given a worksheet to fill out."
    "Ms. Sumner set up the projector just as she did on the first day."
    "It seemed like we might be watching a lot of movies in this class."
    "I could get used to this."
    s "Please enjoy."
    hide sumner with dissolve
    "The movie began rolling."
    "It was called \"Between the Folds\"."
    "Apparently, it was a documentary by Vanessa Gould."
    "I thought it would be an actual movie, rather than a documentary."
    "The documentary began with an interview with some guy named Paul."
    "Paul" "Everything is folded..."
    "Paul" "DNA is folded. So we are born from folding."
    "Paul" "Mountains, valleys, the galaxies... the air, when we talk."
    "How philosophical."
    "Paul" "Sculputres and scientists work in the shadows between art and math."
    "I guess this documentary was on origami or something."
    "Paul" "Anything can be created out of a square block of paper."
    "Paul" "One sqare can be transformed by folding. {w}No scissors. {w}No tape. {w}No glue."
    "The movie then went to a section about \"The Artisan\"."
    "It was about some guy named Michael who folds paper, but also makes it."
    "Apparently he's the only origami artist in the world that also makes the medium (paper) itself."
    "Michael" "Origami is a metamorphic art form."
    "I guess I could see that, since cutting wasn't allowed."
    "Michael" "Cutting paper is subtractive."
    "Michael" "Don't add to it. {w} Don't take away from it. {w} Just change it."
    "Michael" "That way, what you make from a piece of paper... it was there all along!"
    "Interesting."
    "After Michael showed us around his studio, we moved on to \"The Artist\", featuring Michael's friend, Eric."
    show eric at truecenter with zoomin
    "Eric Joisel was described as a patient, French folder."
    "Eric" "I dropped everything, I dropped all other sculptures, just to be an origami artist."
    "Wow."
    "Folding paper seemed fun, but I'm not sure if I would be able to drop everything to become an origami artist."
    "This guy semeed pretty meticulous though. He had a book for planning his folds."
    "We watched him show off his intricate design for his violinist model."
    "Eric" "These two corners become two shoes."
    "Eric" "These five fingers require eight pleats."
    "Eric" "This long hat requires the detail of the face planned out first."
    "Amazing. He also never creates the same place twice."
    hide eric with dissolve
    "The scene then transitioned into \"The Engineer\"."
    "It was about some guy named Robert J. Lang."
    "Apparently held a physics degree from some prestigious university."
    "Robert" "I specialize in technical origami... I chucked my degree into the bin for paper folding!"
    "..."
    "Robert" "I try to create realistic origami, in order to achieve a sense of realism."
    "Robert" "This does not come by trial and error, nor by accident."
    "This guy used mathematical and geometric ideas to achieve the goal of a symmetrically folded shape."
    "I never thought a physicist would ditch their career to do origami."
    "I also never thought someone would be so dedicated to origami so as to plan out every single fold and analyze them mathematically."
    "Robert" "What you can accomplish is strongly governed by mathematical laws."
    "I guess that made sense."
    "Once Robert finished presenting his geometric models for folding, the movie moved onto the scene titled \"The Father\"."
    "This guy was named Akira Yoshizawa, but people called him \"sensei\"."
    p "Yoshizawa was a self-taught man ahead of his time."
    "Apparently this guy was the first origami artist."
    "He abandoned the factory life to interpret the world in paper."
    "The documentary showed one of his works."
    show akira at truecenter with zoomin
    "I thought it was pretty cool."
    p "Yoshizawa used kept his paper wet, a process known as wetfolding."
    p "He also invented the system of diagramming using pictures."
    "We were shown diagrams that looked similar to Eric's more intricate ones."
    p "Yoshizawa created over 50,000 models, but never sold a single one."
    p "He would perform odd jobs, like selling soup door to door."
    "I was impressed."
    "It must take a lot of dedication to quit your day job to spend all day doing origami."
    p "He wished to see origami recognized as an art."
    hide akira with dissolve
    "The video then showed how the complexity of a piece increased over time."
    "In the 60s, there were only around 20 to 30 steps."
    "In the 80s, there were 70 to 90 steps."
    "In 2003, 200 to 300 steps."
    "They predicted that in about 2013, there would be pieces that took 1000 steps to fold from start to finish."
    "The video was then paused."
    show sumner normal at center with dissolve
    s "We're out of time, so we'll stop here for today."
    s "We will finish the documentary tomorrow, and I will hand out the worksheet then."
    s "Don't forget about the essay due next week. {w} Class dismissed."
    "Students began to pack their things."
    hide sumner with dissolve
    "I gathered my things."
    "I looked to my right."
    show dylan normal at right with moveinright
    play music music_dyl_slow fadeout 1.0 fadein 1.0
    d "What?"
    r "..."
    r "Nothing. I'm just surprised you're not asleep."
    show dylan thinking at right with dissolve
    d "Heh."
    d "I may not look like it, but I've always been interested in origami when I was little."
    r "That's surprising to hear."
    "Come to think of it, I used to attend an after school program in grade school, since my mom would always get out of work late."
    "One of the main activities we did was origami."
    "I recall those memories as moments of my life when I was at peace."
    show dylan normal at right with dissolve
    d "Don't tell me you've never done origami before?"
    r "I have."
    d "Then you understand."
    r "Yeah."
    "What was it about origami that made it so pacifying anyways?"
    "I was thinking on the subject, when..."
    d "Food? I'm starving."
    r "Sounds good."
    "So we headed out towards the hall..."
    scene bg hallway with dissolve
    play music music_light fadeout 1.0 fadein 1.0
    show aura normal at center with dissolve
    a "Hey."
    "Look who it is."
    r "Hey."
    show aura sleepy at center with dissolve
    "She glanced towards Dylan's direction."
    hide aura with dissolve
    "... and then disappeared."
    "What was that about?"
    "It was like she ran away."
    "Then again, I heard different classes had different lunch times. I guess she was in a section that had class right now."
    d "..."
    "Dylan was looking at me the whole time, but didn't say anything."
    "He usually would comment on something like that, since I usually don't talk to anyone but him."
    if mentioned_aura:
        "Something like, \"Was that the girl you were talking about earlier?\""
    "Instead, he looked at me quizically. I guess it was due to the fact that I was staring right back at him and saying nothing."
    "I thought he was going to say something, but then he kept walking."
    hide dylan with dissolve
    "I decided to leave it alone."
    scene bg cafeteria with dissolve
    "We got in line."
    "As always, it took forever."
    "Eventually, we sat down and ate."
    "Then it was time to head to Mr. Randall's class."
    show dylan normal at right with dissolve
    d "Wait."
    r "What is it?"
    d "I'm not done yet."
    r "..."
    "I remembered yesterday that I was late for Mr. Randall's class."
    r "I'll go on ahead."
    show dylan thinking at right with dissolve
    "Dylan nodded."
    hide dylan with dissolve
    "I got up and left."
    scene bg corridor_afternoon with dissolve
    "I headed up to the proper floor."
    scene bg math_day with dissolve
    "And entered the proper room."
    "I wasn't late this time."
    show randall normal at center with dissolve
    ran "I'll be collecting the homework now."
    "We passed up our homeworks to the front of the class."
    ran "Thank you. Today, we will learn about..."
    "... I took notes, and stayed awake somehow."
    "......"
    "The bell rung."
    ran "See you all tomorrow."
    hide randall with dissolve
    "I packed my things and left along with the students."
    scene bg corridor_afternoon with dissolve
    play music music_night fadeout 1.0 fadein 1.0
    show dylan normal at right with dissolve
    "Dylan and I exchanged farewells."
    hide dylan with dissolve
    "And then he left."
    "I didn't feel like going home quite yet."
    $ stayed = False
    menu:
        "I..." # it actually doesn't matter; the player will be rerouted to Sumner's class either way for the encounter with Aura.
        "Stay where I am for a while.":
            "I decide to stay in this hallway for a while."
            $ stayed = True
        "Go to Ms. Sumner's class room.":
            "I decide to hang out for a while in home room."
            scene bg hallway with dissolve
            "I walked downstairs..."
            scene bg class_entrance_evening with dissolve
            "... entered the room, which was empty now... "
            scene bg class_evening with dissolve
            "... and sat in the back, as if class was going to start."
    "I waited..."
    "For what, I didn't know."
    if stayed:
        scene bg corridor_night with dissolve
    else:
        scene bg class_night with dissolve
    "But eventually, the sun set."
    if stayed:
        "I decided to head down to Ms. Sumner's class room for some reason."
        scene bg hallway_night with dissolve
        "I walked down the stairs..."
        scene bg class_entrance_night with dissolve
        "... and entered the room, which was pretty much empty by now..."
        scene bg class_night with dissolve
        "... and sat in the back, as if class was going to start."
    "I looked outside, and could see the bright moon in the sky."
    "..."
    "I decided to go home."
    scene bg class_entrance_night with dissolve
    "I made my way to the door."
    "I grabbed the door handle, about to turn."
    "... when out of the corner of my eye, I noticed something."
    show aura he at left with dissolve
    stop music
    "..."
    "I turned so that the figure was in front of me."
    show aura he at center with dissolve
    "I was completely shocked by her appearance that I forgot to ask if she really did go to this school."
    r "Haven't classes ended a while ago?"
    show aura shock at center with dissolve
    play music music_aura
    a "Have they?"
    a "Hmm..."
    "She pretended to think."
    show aura slight_surprise with dissolve
    a "I guess they have..."
    "..."
    "She seemed kind of dense."
    "I didn't know if it was an act, or if she really was this out of touch with reality."
    show aura normal with dissolve
    a "But the same goes for you."
    a "Why are you still hanging around?"
    "I take that back. She's only {i}slightly{/i} out of touch with reality."
    menu:
        "I..."
        "Was hanging around.":
            r "I just decided to hang around."
            a "I see..."
        "Thought you'd be here.":
            $ pt_a += 1 # POINT_AURA max: 4
            r "I thought that you would be here."
            show aura happy with dissolve
            a "Ahahahaha!"
            a "Well, you were right!"
    show aura enthusiastic at right with dissolve
    a "Well, now that you're here, let's play!"
    r "... play?"
    show aura happy at right with dissolve
    a "Yeah!"
    "She reached into her bag pockets and pulled out what looked like crumpled up pieces of paper."
    "No, they weren't crumpled up..."
    show origami at truecenter with dissolve
    "... they were folded."
    r "Origami...?"
    a "Mhmm!"
    "The girl with the odd-colored hair gave me a piece that had yet to be folded."
    "I took it from her hands slowly."
    show aura enthusiastic at right with dissolve
    a "Let's make something cool!"
    "How long has it been since I had done this?"
    "I looked at the paper in my hands."
    "Then I looked up at Aura."
    show aura concentrating at right with dissolve
    "She was concentrating hard on shaping the paper into something meaningful."
    "..."
    "Might as well."
    "First I folded the paper in half."
    "Then I folded a corner of it to one side. {w} This will be the beak."
    "I pulled apart the flaps of paper from the initial fold and bent them backwards."
    "Carefully folding the flaps back, I made small, incremental creases to mimic ruffled feathers."
    "..."
    "After a few more folds, I was done."
    "I looked up."
    "It looked like Aura was just about finishing up as well."
    show aura happy at right with dissolve
    a "All done!"
    r "Yeah, me too."
    a "Lemme see! Lemme see!"
    "I showed her my paper crane."
    show aura enthusiastic at right with dissolve
    a "Wow! It's like the real thing!"
    r "Eh..."
    "I thought it resembled more of an airplane with an unnaturally long tail."
    "I wonder what Aura made."
    r "Can I see yours?"
    show aura normal at right with dissolve
    a "Mhm!"
    "She handed over her work of art."
    "... or what was supposed to be a work of art."
    "I remember back when I was in elementary school, the boys would always crumple up unused paper and throw it into the wastebin from a distance, simulating playing basketball."
    "What Aura handed to me looked exactly like that."
    "A compressed and crumpled up paper basketball, to be tossed into the garbage from a distance."
    show aura enthusiastic at right with dissolve
    a "Isn't it great?!"
    r "Er..."
    r "Yeah, it's pretty good. It looks exactly like a..."
    "... like a what?"
    "What was it even supposed to be?"
    a "A boat?"
    r "Sure."
    show aura happy at right with dissolve
    a "Ahahahaha!"
    a "That's exactly what I was aiming for!"
    "..."
    "I imagined small paper people trying to ferry this \"boat\" across a bathtub, only for it to sink to the bottom like a rock."
    "Maybe if the center were pressed down and flattened a bit, it would resemble a boat more."
    "But I didn't want to mess with her work of art."
    show aura normal at right with dissolve
    a "We should probably start heading home now."
    r "Yeah, it's getting late."
    hide origami with dissolve
    "Aura put her origami boat/rock/basketball into her pockets."
    "I stowed mine away in my bag."
    show aura happy at right with dissolve
    a "See ya!"
    hide aura with dissolve
    "... and with that, she ran out the door."
    "Although it seemed like she was running, I couldn't hear any footsteps leaving the hall."
    "I decided to head home myself."
    show bg hallway_night with dissolve
    play music music_night fadeout 1.0 fadein 1.0
    "I headed out into the hallway."
    show bg park_night with dissolve
    "I passed the park on the way home."
    show bg house_night with dissolve
    "And finally got home."
    show bg bed_night with dissolve
    "I was exhausted."
    "I realized that I had an essay to write."
    "Today was my third day of school, a Wednesday, and it was assigned yesterday, on the second day."
    "This meant it was due next week on Tuesday."
    "Counting tomorrow, I only have five days to write it."
    "Too tired to come up with any ideas for it now, all I wanted to do was sleep."
    "Somehow, I managed to do my math homework."
    scene black with dissolve
    stop music fadeout 1.0
    "But I fell asleep shortly after."
    jump day_4
    
label day_4:
    "..."
    m "-eading out! Make sure you wake up for school!"
    "I could hear the end of my mom's phrase, and then a door slamming as the house fell silent."
    scene bg bed_day with dissolve
    play music music_bed
    "I opened my eyes."
    "Today was the fourth day of school."
    "I packed the math homework I stayed up late doing last night, and got ready."
    scene house_day with dissolve
    "I headed downstairs."
    "And headed outside."
    scene bg park with dissolve
    "It was a nice day for a walk."
    scene bg park_day with slideleft
    "There were two children playing at the park."
    "But other than that, no one else was there."
    scene bg park with slideright
    "I kept walking."
    scene bg school_entrance with dissolve
    "And eventually reached the school's entrance."
    "Thursday."
    "I joined the swarming colony of students migrating through the gates."
    scene bg hallway with dissolve
    "I made my way to class 2A, passing Dylan on the way."
    show dylan thinking at right with dissolve
    play music music_dyl_slow
    "... he seemed to be asleep."
    "He was standing right outside the door, too."
    "He didn't even make it into the classroom."
    $ wokeup = False
    menu:
        "I..."
        "Wake him up.":
            $ wokeup = True
            $ pt_d += 1 # POINT_DYLAN max: 4
            r "Hey."
            d "..."
            r "Heeeeeeey."
            d "..."
            r "HEY."
            d "Huh."
            show dylan normal at right with dissolve
            d "Oh. Sup."
            r "Don't \"sup\" me. You fell asleep."
            d "Oh."
            r "You would've been late again."
            d "Haha, thanks for waking me."
            "I gestured with my hands that it was no problem."
            "We both walked inside."
            hide dylan with dissolve
        "Don't wake him up.":
            "I'll let him sleep a little while longer."
            "Maybe he had a long night."
            "I headed into class by myself."
    scene bg class_entrance_day with dissolve
    play music music_class fadeout 1.0 fadein 1.0
    if wokeup:
        "We entered class at the perfect time, neither early nor late."
        "We sat down in the back as always."
    else:
        "I entered class at the perfect time, neither early nor late."
        "I sat down in the back as always."
    scene bg class_day with dissolve
    "As the classroom populated with students, Ms. Sumner walked to the front of the room."
    s "Okay class. Good morning."
    if wokeup:
        "Today, we will be finishing up the movie."
    else:
        "Today, we will be finishing up th-"
        show dylan thinking at right with moveinright
        play music music_dyl_slow
        "The door opened, and everyone's eyes shifted to Dylan, the only one standing in the path."
        d "*yaaaaaaaaaawwwwwwn*"
        "..."
        "Dylan dragged his feet across the room and joined me in the back."
        "I think he was still asleep."
        hide dylan with moveoutright
        "He put his head down, and if he wasn't asleep before, now he was."
        play music music_class fadeout 1.0 fadein 1.0
        s "..."
        "Ms. Sumner was speechless."
        s "Anyways. Today we will be finishing up the movie."
    "Ms. Sumner set up the projector and stepped back to her desk while the movie played again."
    hide sumner with moveoutleft
    "Yesterday we left off with the guy who basically invented origami."
    "Now the scene was transitioning to \"The Bug Wars\"."
    p "There are now programs for modelling orgami figures."
    "The film talked about how math and science were related to origami."
    p "Mathematical terminology can be used to describe the paper, such as what ideal proportions to use, and what algorithms should be used to get a certain type of fold."
    p "At first, we must learn the art. We must learn the technical details."
    p "At first, we must get through the phase of no emotion, in order to get to the end."
    p "However, as we get older and mroe experienced, we tend to take out the technique, and keep just the emotional things."
    "That makes sense."
    "Learning something for the first time sure did require a kind of mechanical feel to it."
    "But after we got used to doing it, we could freely experiment."
    "The documentary then transitioned scenes into one titled \"The Postmodernist\"."
    "I didn't really pay that much attention, but the one thing that caught my eye was that some origami artists used exactly only one fold in some of their works."
    "The scene after that, \"The Choreographer\", was what was really amazing."
    "Some guy named Chris Palmer specialized in orgami that changes with movement."
    "The paper he folded held a lot of tension and potential energy, so that at even the slightest disturbance, it would spring up."
    "I guess that was one way you could incorporate physics into origami."
    # PICTURE: LE CRIMP
    show lecrimp at truecenter with zoomin
    "The section after that, \"les Anarchistes\", talked about a \"le crimp\" style of origami."
    "Using this style, origami artists would crumple the paper freely, and thus create work born from chaos."
    "What surprised me was a scene that followed: \"Functional Form\"."
    "The film showed how a small group of around 200 physicists, computer scientists, biologists, and mathematicians come together annually to talk about origami."
    "The fact that so many people of technical expertise would come together to perform an art was amazing."
    "They then showed a woman who went to Israel and used origami to teach geometry to children."
    "I thought that was pretty nice."
    p "Making origami is at heart an engineering problem."
    p "Origami artists must always keep in mind the question, \"How can I get the paper to do -this-?\""
    "I stopped paying attention when the film started talking about concentric squares folded to form a hyperbolic paraboloid ..."
    "..."
    "I think the documentary was at its final section now."
    "\"The Theory of Everything\", they called it."
    "The main character this time was a professor named Erik Demaine."
    "Apparently he had many eccentric hobbies such as blowing glass and making furniture with books."
    "Along with that, he was involved in computational geometry research."
    p "Demaine used the work developed by Robert Lang, who designed origami with a computer, to solve problems in computational geometry."
    p "In a way, origami is like a computer program."
    p "Putting a crease or a fold in a paper changes the \"memory\" of the paper."
    "I thought that was pretty interesting."
    "But then I soon got lost, as they began discussing the Folding Cut Problem."
    hide lecrimp with dissolve
    "The film closed with some applications of origami."
    p "Even aesthetics can come to have applications."
    # PICTURE: AIRBAG
    show airbag at truecenter with zoomin
    p "Consider the algorithm for flattening an airbag, so that we can conserve space in cars."
    p "This algorithm comes from the designs of artistical origami."
    "I suppose having a huge air bag take up a bunch of space in the front of a car wouldn't be practical."
    # PICTURE: PROTEIN FOLDING
    hide airbag with dissolve
    show protein at truecenter with zoomin
    p "Additionally, mathematical models can be developed for how proteins fold."
    p "This protein could be developed into a custom drug that fights particular viruses."
    "I remember in a biology class I took before that diseases and viruses were sometimes caused by a protein folding incorrectly."
    "I think there was some new technology that enabled something called protein prediction, where we could cure viruses and disease before they even came."
    "So this is where origami had its applications..."
    p "We are all artists whether we do science, or whether we build sculpture."
    hide protein with dissolve
    p "The power of origami is simplicity: it allows everyone to create their interpretation of the world on paper."
    "And with that, the film played the credits and was stopped by Ms. Sumner."
    show sumner normal at center with dissolve
    s "And that was the film."
    s "What did you all think of it?"
    "There was murmer amongst the class."
    "I thought it was pretty interesting."
    "I didn't know that origami was that intricate. I always just did it for fun."
    "Speaking of which, it was only yesterday that I was making origami with Aura."
    "I wonder if she thought about the intricacies of origami."
    "... Probably not."
    s "As I said before, I will now hand out a worksheet to fill out for this movie."
    "A large stack of paper was passed around the class."
    "When it came around to me, I took one and passed the remainder of the stack to my right to Dylan."
    show dylan normal with moveinright
    d "Thanks."
    hide dylan with moveoutright
    "I looked at the worksheet."
    "\"{i}Between the Folds{/i} Worksheet\", it was titled."
    "I looked at some of the questions."
    "\"Do you observe 'workable bridges between art and science' in the documentary? If so, how and where?'"
    "There were seven other questions, all with increasing complexity."
    "I guess I know what I'll be doing over the weekend."
    s "Please work on it and have it ready by next week on Thursday."
    "So we had a week."
    s "Also, please remember that your essays are due next Tuesday."
    "Great."
    "I haven't even started on that one, and it's already been two days."
    "I didn't even know what I would write about."
    s "Class dismissed."
    "People began shuffling out."
    "I headed out as well, with Dylan following behind."
    scene bg hallway with dissolve
    play music music_light fadeout 1.0 fadein 1.0
    "We headed to lunch."
    scene bg cafeteria with dissolve
    "Got in the arduously long line as usual."
    "Sat down and ate food as usual."
    scene bg corridor_afternoon with dissolve
    "Then headed to Mr. Randall's class as usual."
    scene bg math_afternoon with dissolve
    "..."
    hide dylan with dissolve
    show randall normal at center with dissolve
    "We handed in the homework."
    "Listened to lecture."
    "Until the bell rung."
    ran "Have a nice day."
    hide ran with dissolve
    "And then we all flocked to the exit."
    # going home, day 4. we skip day 5?
    play music music_night fadeout 1.0 fadein 1.0
    scene bg corridor_afternoon with dissolve
    show dylan normal at right with moveinright
    d "See ya."
    r "Yup."
    hide dylan with dissolve
    "I began to walk home."
    scene bg park_evening with dissolve
    "The park was quiet as always."
    "I looked around."
    "It didn't seem like anyone was here at this time."
    scene bg house_day with dissolve
    "I arrived home."
    scene bg bed_day with dissolve
    "I unpacked my things and started to get working on math homework."
    "..."
    "After finishing, I tried to think about what else I needed to do."
    # OPTION: work on essay vs work on worksheet?
    "I decided to work on my essay."
    "... though, I couldn't really think of anything."
    "..."
    "I really couldn't think of what to write."
    "\"Reflect on Elkins' and Snow's articles, and explain how they are relevant in your daily lives.\""
    "The articles were about the seperation of two cultures."
    "Art and science."
    "How did that apply to my daily life?"
    "..."
    "I didn't know."
    scene bg bed_night with dissolve
    "I turned off the light."
    "Maybe it'll come to me tomorrow."
    "..."
    scene black with dissolve
    stop music fadeout 1.0
    "..."
    #jump day_5
    # we will skip day_5, nothing interesting will happen. (author: I can't think of anything to write for it)
    jump weekend_1
    
    
label weekend_1:
    "Friday was pretty boring."
    "It was the same old routine."
    "I'll spare the details."
    play music music_pondering
    scene bg bed_day with dissolve
    "I got up like usual."
    scene bg house_day with dissolve
    "Went downstairs like usual."
    scene bg park with dissolve
    "Walked to school like usual."
    "..."
    scene bg school_entrance with dissolve
    "Arrived to school like usual."
    scene bg hallway with dissolve
    "..."
    scene bg class_entrance_day with dissolve
    "..."
    scene bg class_day with dissolve
    "..."
    show sumner normal at center with dissolve
    "... listened to Ms. Sumner lecture like usual."
    "I think she said something about beginning a new topic next week."
    "... even though we still had two assignments due from the first week."
    hide sumner with dissolve
    "Oh well."
    scene bg hallway with dissolve # does this even go through? does the user pause?
    scene bg cafeteria with dissolve
    "..."
    show dylan thinking at center with dissolve
    "... ate lunch with Dylan as usual."
    hide dylan with dissolve
    scene bg corridor_afternoon with dissolve
    "..."
    scene bg math_afternoon with dissolve
    "... handed in my daily math homework as usual."
    show randall normal at center with dissolve
    "... listened to Mr. Randall drone on about properties of numbers that I found to be pointless."
    hide randall with dissolve
    scene bg corridor_afternoon with dissolve
    "..."
    scene bg park_evening with dissolve
    "... headed home as usual."
    scene bg house_day with dissolve
    "..."
    scene bg bed_day with dissolve
    "... again, tried to think about what to write for an essay."
    "Though, I figured I had the weekend for it and so didn't spend too much time on it."
    "In the end, I had wasted a bunch of time doing nothing."
    scene bg bed_night with dissolve
    "... and, of course, in the end, I didn't work on my essay at all."
    scene black with dissolve
    "Over the weekend I didn't really do much."
    "I think I watched TV for a bit."
    "Maybe read a few comics."
    "I finished the worksheet on that Folds video that we were assigned."
    "..."
    "Before I knew it, it was Monday of the second week already."
    "I hadn't started my essay."
    stop music fadeout 1.0
    jump week_2_1

#We'll start naming labels by week instead of day now. i.e., week_<week#>_<day#>.
label week_2_1:
    "..."
    "......"
    m "I'm heading out!"
    play music music_bed fadein 1.0
    scene bg bed_day with dissolve
    "My mom's farewell woke me up."
    "I got out of bed and got ready."
    scene bg house_day with dissolve
    "And started heading out."
    play music music_day fadeout 1.0 fadein 1.0
    scene bg park with dissolve
    "On my way to school, I felt something light in the air."
    "..."
    scene bg park_day with slideleft
    "... It was coming from this direction."
    show aura sleepy at left with moveinleft
    "!"
    hide aura with moveoutleft
    "I thought I saw something out of the corner of my eye."
    scene bg park with slideright
    "I quickly turned."
    "... but there was nothing there."
    #OPTION: wait around for Aura? paralellism?
    "I kept on walking to school."
    scene bg school_entrance with dissolve
    "All of the students shuffling in through the school doors looked like zombies."
    "It probably had something to do with the fact that today is Monday."
    "I probably looked the same as them."
    scene bg hallway with dissolve
    "I headed to class 2A."
    show dylan normal at right with moveinright
    play music music_dyl
    "... this was probably the only guy who didn't look like a zombie."
    d "Yoooo."
    r "Hey."
    show dylan thinking at right with dissolve
    d "Where were you this weekend?"
    r "At home."
    d "I tried calling you?"
    r "You did?"
    "..."
    "I never heard my phone ring."
    "Oh, that's right."
    "I think my mom mentioned something about the phone line being down in my area or something."
    r "I think the phone line is down in my area."
    d "Oh. That's a shame."
    "So that's why I didn't get any calls."
    r "I didn't really do much anyways."
    d "Yeah, me neither."
    r "Hahahaha."
    show dylan normal at right with dissolve
    d "Ahahahahaha."
    hide dylan with moveoutright
    scene bg class_entrance_day with dissolve
    play music music_class fadeout 1.0 fadein 1.0
    "We headed into class chuckling dryly."
    scene bg class_day with dissolve
    "And sat in the back as usual."
    "..."
    "Eventually, it was time for class to start."
    show sumner normal at center with dissolve
    s "Good morning class."
    s "Welcome to the second week of school."
    s "Like I mentioned last week, we will begin a new topic this week."
    s "Moving away from the definition of aesthetics and examining the joint efforts between artists and scientists in that field, we will instead look at something called contemporary aesthetics."
    s "We will look at examples of aesthetics in the world today."
    s "The main example we will focus on this week is a poem called \"Howl\" by Allen Ginsberg."
    s "We will read the poem most likely in the middle of the week, and then watch a movie adaptation towards the end of this week."
    s "But first, let us begin with two introductory videos to this week's topic."
    #Synthetic Aesthetics: Daisy Ginsberg
    "Ms. Sumner set up the projector and moved back to her desk as the clip began playing."
    "The film was about something called the \"E. Chromi Project\"."
    "The speaker was a woman named Daisy Ginsberg."
    "Daisy" "We aim for future self-diagnoses of internal ailments through drinkable, synthetically engineered probiotics."
    "That sounded intense."
    "So would that mean that there would be no more need for doctors?"
    "I wonder what that would do to the medicine market."
    # PICTURE: E. Chromi Project. colored poop?
    show echromi at truecenter with zoomin
    "Daisy" "We would be able to tell what our problems are from our colored poop."
    "Umm... what?"
    "Daisy" "We ask, can {i}design{/i} contribute towards biological computation, and programmable bacteria?"
    "Daisy" "There is a lot cut back by {i}policy{/i}."
    "The presenter then gave an example of one of those innovations cut back by policy called the \"Growing Plant Project\"."
    "Apparently they got $500,000 from funders to make glowing plant seets, but then they got shot down by the law once the funders got the seeds in the mail."
    "Daisy" "We would be designing life, and living things."
    "And the video came to a close."
    hide echromi with dissolve
    "The idea sounded pretty interesting. But it was a bit of a stretch."
    show sumner normal at center with dissolve
    "Ms. Sumner walked to the center of the room."
    s "You may all think that the ideas presented in this video were far-fetched."
    s "But that was the point - this video was shown to stretch your minds, and show the power of innovation."
    s "If you have a good idea, a good design, and have enough supporters, you can even save lives."
    "..."
    s "And now, we will move on to the second video."
    #Richard Shusterman's Somaesthetics: Thinking Through the Body
    hide sumner with dissolve
    "Ms. Sumner moved back to her desk again as the video began playing on the projector."
    "The words \"Somaesthetics: Thinking Through the Body\" were displayed on the screen."
    "The presenter was some guy amed Richard Shusterman."
    # PICTURE: SOMAESTHETICS
    show somaesthetics at truecenter with zoomin
    "Shusterman" "The body is not just a piece of flesh or a machine."
    "Shusterman" "Aesthetics is not only theory of beauty."
    "Shusterman" "It's actually a Greek word for \"sensory perception\". Take for example, the word \"anesthetics\"."
    "Shusterman" "The body is universal. We must make sure not to misuse it, like for profiling races, maybe in a prejudicial way."
    "Shusterman" "Instead, we should use the body to express one's values and to style one's self."
    hide somaesthetics with dissolve
    "He then talked about one of the books he wrote, and then the film ended."
    show sumner normal at center with dissolve
    s "Shusterman is known for introducing the concept of somaesthetics."
    s "Somaesthetics is the philosophy of using the body and its senses to enrich our mind and experience the world."
    s "Anyways, it looks like time is up for today."
    s "Remember that the essay assigned last week is due tomorrow."
    s "Class dismissed."
    "... Right, the essay."
    "I still hadn't come up with what to write for that."
    hide sumner with dissolve
    "I decided to ask Dylan what he wrote about to see if I could get some ideas."
    show dylan normal at right with moveinright
    play music music_dyl
    r "Hey."
    d "Sup."
    "He looked like he had just woken up."
    r "Did you start the essay yet?"
    d "What essay?"
    "..."
    "Don't tell me..."
    r "... You know we have an essay due tomorrow right?"
    d "We do?"
    r "..."
    show dylan thinking with dissolve
    d "Hmm..."
    "He closed his eyes and thought for a while."
    "All of the students had left the classroom already."
    d "So, what was the topic?"
    r "We had to write about how those two readings from last week applied to our daily lives."
    show dylan normal with dissolve
    d "What readings last week?"
    "..."
    "This guy was beyond any hope."
    r "Nevermind."
    "I should have known Dylan wouldn't have started the essay."
    "He probably wouldn't even write it."
    "He was notorious for not doing any work in middle school."
    "To be honest, I'm not even sure how he passed."
    #hide dylan with moveoutright
    play music music_day
    scene bg hallway with dissolve
    "We headed out into the hallway, and made our ways to the cafeteria for lunch."
    scene bg cafeteria with dissolve
    "We were a bit late, so there wasn't much of a line this time."
    "But as a result of being late, that also meant we didn't have much time to eat."
    "I got something light and ate it quickly."
    show dylan thinking at right with dissolve
    d "..."
    "On the other hand, Dylan had no regard for the time and purchased a huge meal."
    "Mr. Randall's class was about to start soon."
    r "I'm going ahead."
    d "See ya."
    "He kept stuffing his face."
    hide dylan with dissolve
    scene bg corridor_afternoon with dissolve
    "I left Dylan behind and headed towards class."
    scene bg math_day with dissolve
    "I handed in my homework as per usual, and sat down in the back."
    show randall normal at center with dissolve
    "Mr. Randall lectured on and on."
    "..."
    # throw this in on Monday
    "Though, during the whole class, the only thing I could think about was the impending essay I had due."
    # aura helps with essay
    "The bell finally rung for the dismissal of school."
    ran "We will finish up learning how to find the determinant of a matrix tomorrow."
    hide randall with dissolve
    "I began to gather my things."
    "I don't think Dylan ever ended up making it to class."
    scene bg corridor_afternoon with dissolve
    "I began to walk home, dreading how I would have to start and finish an essay in just a day."
    "And I didn't even have any ideas to go off of to begin it."
    show aura normal with dissolve
    a "You're taking a math class with Mr. Randall and learning about art and stuff with Ms. Sumner, aren't you?"
    r "Yeah..."
    stop music
    "Wait a second."
    show aura happy with dissolve
    play music music_aura
    r "You again!"
    a "Me again!"
    "What is she doing here?!"
    r "I thought you didn't go to this school?!"
    "That's right - last week, I had forgotten to ask her that question since I had been so surprised by her appearance."
    show aura normal with dissolve
    a "I don't!"
    r "Then what are you doing here?"
    a "I guess I'm going to this school..."
    r "..."
    a "..."
    r "..."
    show aura nervous with dissolve
    a "..."
    r "... Oh forget it."
    show aura happy with dissolve
    a "Haha!"
    r "So what class room are you in?"
    show aura normal with dissolve
    a "That's a seeeeecret!"
    r "Uh... okay."
    "... What does she want?"
    "Oh wait."
    r "Wait. You were saying something about Mr. Randall and Ms. Sumner?"
    show aura enthusiastic with dissolve
    a "Yep! You were stuck writing an essay comparing scientists and artists, right?"
    "How did she know?"
    "Regardless, it seemed like she was onto something, so I just played along."
    r "Yeah..."
    a "Well!"
    show aura concentrating with dissolve
    "She seemed to be focusing really hard on something."
    a "Mmmmm..."
    r "...?"
    show aura happy with dissolve
    a "I got it!"
    #Robert J Lang - engineer from The Folds - what you can accomplish in art is strongly governed by mathematical laws
    a "According to Robert Lang, the engineer in that video, \"what you can accomplish in art is strongly governed by mathematical laws!\"."
    "Whaaaaaaat?"
    "How did she have that great of a memory?"
    "Wait, first of all, how would she even know about that video?"
    "I had overheard from other students that different classes had different material taught."
    "And it seemed that no other class except for ours had watched that movie."
    "Part of it was the school's method to prevent plagiarism, or at least to pinpoint plagiarism down to the classroom level. As in they wouldn't have to search the whole school if two assignments looked too similar."
    "So even if Aura did go to this school, there's no way she would have known what was in the video unless she was in my class."
    "Even so, I decided not to question her right now."
    r "What about it?"
    a "So, you're taking a math class right now. And an art class. Don't you think that what you can do in art is limited by your knowledge in math?"
    a "Remember when we folded origami last week?"
    a "You only could've made that shape, I think it was a crane, since you knew of underlying structure of that object."
    "... I didn't know she was capable of big words such as \"underlying\". Is this the same Aura that I know?"
    a "Furthermore, because now you know the nature of triangles and how the geometric patterns work, you can visualize better how to fold origami than you could have when you were in kindergarten."
    "That made sense... wait, how did she know how I folded origami in kindergarten?!"
    r "Wait. How do you know how I folded origami in kindergarten?"
    show aura nervous with dissolve
    a "Err..."
    "... She stood there and gave no reply."
    r "You're really creepy, you know."
    show aura happy with dissolve
    a "Hah! Anyways, just hear me out!"
    a "So in your essay, you could talk about how you agree with Snow about the marriage of the two arts from your experience with arts and crafts."
    a "And you could explore his idea that the school education is too specialized, and throw in the fact that you're taking two different classes right now, one in each \"culture\"."
    a "And with the pessimistic Elkins, you could argue how the two cultures shouldn't seperate, but instead work together."
    "... That's a brilliant idea."
    r "Wow. Why didn't I think of that?"
    show aura normal with dissolve
    a "But you did!"
    r "Huh? What do you mean? You basically just told me what to write."
    a "But I bet you probably had it in you all along."
    "... I didn't quite believe that."
    show aura happy with dissolve
    a "Anyways, good luck with your essay!"
    r "Hey, wait!"
    a "See ya!"
    hide aura with dissolve
    "..."
    play music music_night fadeout 1.0 fadein 1.0
    "I didn't quite understand what had just happened."
    "A billion thoughts raced through my mind."
    "... I was so busy sorting out my thoughts, that I just realized that I forgot to thank her."
    "Anyways, with a new idea in my mind now, I started brainstorming what I could possibly write."
    scene bg park_night with dissolve
    "Hmm... maybe I'll throw in an example of how the notion of \"elegance\" can exist in both cultures as well."
    "I didn't even notice how dark it was until I walked by the park."
    "... did I really spend that much time talking to Aura?"
    "I needed to get back soon in order to finish the essay."
    scene bg house_night with dissolve
    "I arrived home and quickly jolted upstairs."
    scene bg bed_day with dissolve
    "I began writing my essay."
    "Words blazed across my screen faster than I thought was possible."
    "..."
    "It took a while, but I was finally done."
    scene bg bed_night with dissolve
    "I shut off my main bedroom light."
    "I kept thinking back to today's encounter with Aura."
    "What did she mean by \"I had it in me all along?\""
    "And how could she have known what the film was about?"
    "But moreso, given an exact quote from the film?"
    "Even moreso, known what the assignment was?"
    "... I decided I would ask her the next time I saw her."
    stop music fadeout 1.0
    "I dozed off into a deep sleep."


label week_2_2:
    #Reading 1: Dick Higgins: Synesthesia and Intersenses: Intermedia
    
    ## class
    show sumner normal at center with dissolve
    s "Today, we will be learning about a topic called \"intermedia\"."
    s "The focus will be on a reading by Dick Higgins."
    "Ms. Sumner passed a stack of papers to the student in the front."
    "That student took one page, and passed the rest of the stack around."
    "..."
    "When the stack came to me, there were only maybe five or six pages of paper left. I took one and passed it to my right to Dylan."
    d "Thanks."
    "I looked down and read the title of the article."
    "\"Synesthesia and Intersenses: Intermedia\", it read."
    s "Since this is a short article, I will go ahead and read it out loud to the class."
    "That was a first."
    "Usually we were told to read the articles on our own."
    "Ms. Sumner seemed to command a more active role in our learning today."
    s "Much of the best work being produced today seems to fall between media..."
    "She began."
    "From what I could tell, intermedia seemed like a mixing of multiple art forms."
    "Like a character in a movie painting a picture."
    "Or a character in a movie singing."
    s "\"Dividing arts into groups is like dividing people into groups and classes.\""
    s "\"For example, artisans, serfs, nobility, and landless workers.\""
    s "\"The marriage of arts will bring people together, rather than separate them into categories.\""
    s "\"But we're approaching a classless society.\""
    s "\"Millionaires eat at local pubs. Mayors walk to work during transportation strikes.\""
    "Come to think of it, I did hear time and time again about very wealthy individuals eating in small restaurants."
    "They left tips in the forms of hundred dollar bills though."
    "The article then talked about some artists named Duchamp and Picasso."
    "But what really interested me was this guy named Rauschenberg."
    # PICTURE: "combines" by Rauschenberg - goat with tire around neck splattered with paint
    hide sumner with dissolve
    show combines at truecenter with zoomin
    s "\"In Rauschenberg's \"combines\", one of his works features a painted stuffed goat with a rubber tire around its neck.\""
    "I couldn't believe this was actually considered art."
    "But I guess I could see it. I suppose it is."
    hide combines with dissolve
    # PICTURE: google "stacked deck higgins 1958" yellow picture
    show stackeddeck at truecenter with zoomin
    s "\"In \"Stacked Deck\", the cues are in the audience, and so audience-performer division is removed.\""
    "\"Stacked Deck\" was one of this Higgins guy's operas." 
    "Apparently all of the cues for the performers were based on reactions from the audience."
    s "\"In the works of Nam June Paik and Benjamin Patterson, musical events were replaced by non-musical actions.\""
    s "\"There is intermedia between collage, music, and theater.\""
    s "\"Each work determines its own medium and form according to its needs.\""
    hide stackeddeck with dissolve
    # http://www.mechanicalbrides.com/concretepoetryfigureground.html one of these pictures (last one?)
    # PICTURE: intermedia
    show intermedia at truecenter with zoomin
    "And the article closed off with the definition of intermedia."
    "Surprisingly, I found that my assumptions were wrong."
    s "\"Intermedia involves mixed works, but one in which you can't tell the difference between the works.\""
    s "\"A non-example of antimedia would be a picture of a poem with decor around it.\""
    "That was the mistake I made in assuming what the definition of intermedia was."
    s "\"However, an example of true intermedia would be a poem-like sequence of pictures with a grammar of its own.\""
    s "\"That is, it could be the case that each picture represents a word.\""
    "That seemed extremely complicated."
    "Though, if intermedia were something as simple as throwing a bunch of art from different fields together, we wouldn't be learning about it."
    hide intermedia with dissolve
    show sumner normal at center with dissolve
    s "And that concludes today's class. We will be reading the poem {i}Howl{/i} tomorrow."
    s "Class dismissed."
    "I packed my things and began heading to lunch."
    ## lunch
    

label week_2_3:
    # HOWL poem
    ## class
    s "Welcome to class."
    s "Like I mentioned earlier this week, we would be reading a poem called {i}Howl{/i} by Allen Ginsberg."
    "Like yesteday, a stack of papers was passed around."
    "This time, it looked like there were multiple papers rather than just one."
    "This must be one long poem."
    "..."
    "Once everyone had the poem on their desk, Ms. Sumner began speaking again."
    s "This poem is best read out loud, and so I will do the honors."
    "This would be the second day in a row Ms. Sumner reads to us."
    s "Anyways, let us get started."
    #show sumner glad
    "She took a deep breath and began reading."
    play music music_complex fadeout 1.0 fadein 1.0
    #PICTURE: Howl?
    s "\"I saw the best minds of my generation destroyed by madness, starving hysterical naked, ...\""
    "Ms. Sumner seemed like she was in a trance while she was reading the poem."
    "There seemed to be a lot of sentences starting with \"who\"."
    "... In fact, it seemed like every line began with \"who\"."
    "And I think the author was addressing some guy named Carl Solomon."
    s "\"Ah, Carl, while you are not safe, I am not safe, and now you're really in the total animal soup of time--\""
    "Total animal soup of time? What does that even mean?"
    "I tried to think about what it meant, until I realized that the sentences weren't starting with \"who\" anymore."
    "... the word was still being repeated, but this time it was \"Moloch\"."
    s "\"Moloch whose mind is pure machinery! Moloch whose blood is running money!"
    "Whoever this Moloch was, he didn't seem like a nice guy."
    s "\"Moloch whose eyes are a thousand blind windows! Moloch whose skykscrapers stand in the long streets like endless Jehovahs!"
    "The poem then transitioned once again."
    "At least, that's what I thought, since \"Moloch\" wasn't being repeated anymore."
    "Now, it seemed like the author was finally \"with\" this Carl Solomon."
    "In .... Rockland, I suppose."
    s "\"I'm with you in Rockland, where you imitate the shade of my mother.\""
    s "\"I'm with you in Rockland, where we are great writers on the same dreadful typewriter."
    play music music_class fadeout 1.0 fadein 1.0
    "And with that, the poem was finished."
    #show sumner normal
    s "There is one more part, called the \"Footnote to Howl\", but it is not present in this print."
    s "Carl Solomon, mentioned a lot in this poem, was a psychiatric patient in the Columbia Presbyterian Psychological Institute."
    s "The author of the poem, Ginsberg, met him there when the former pleaded insanity after being falsely arrested."
    s "Solomon reminded Ginsberg of his schizophrenic mother who was lobotomized."
    "Ms. Sumner went on to explain what \"Moloch\" was."
    s "Moloch was an ancient god that had to do with child sacrifice."
    s "Does anyone know what Moloch represented in the poem?"
    "Of course, the student in the front raised her hand."
    "Classmate" "It seemed like Moloch represented everything that freedom was not."
    "Classmate" "There was a lot of mentioning of machines and machinery."
    s "Yes. Moloch represented many things, such as machinery, war, sacrifice..."
    s "Some may even argue that Moloch stood for capitalism, government, religion, and authority in general."
    s "One can think about the \"Rockland\" place at the end trapping poeple, and the escape from this place represents freedom."
    "It did seem like there was a lot of want of freedom in the poem."
    "From the amount of sex, drugs, and alcohol, it seemed like the author praised those who did what they wanted."
    "And it looked like they travelled a lot too, going off of the many places listed in the poem."
    "I thought it was interesting how they compared those are on top of the world, like politicians, capitalists, religious figureheads, and such, to machines."
    "Machines that conform to the standard norm."
    s "It looks like it's time for lunch."
    s "We will cover one more reading tomorrow before watching the movie adaptation on {i}Howl{/i} on Friday."
    s "Class dismissed."
    "I began making my way to hall."
    ## lunch
    
label week_2_4: 
    # Saito Reading: Everyday Aesthetic Qualities and Transience
    s "Good morning."
    s "We read Ginsberg's poem yesterday, but we will hold off on the movie until tomorrow."
    s "Today, we will read an article by Yuriko Saito."
    "A stack of papers was passed around."
    s "Please do the reading on your own. We will discuss in a few minutes."
    "I thought it was strange that Ms. Sumner had read to us for the past two days."
    "I was a bit thrown off by having to read on my own, but I should have expected as much."
    "I peered down at my handout."
    "\"Everyday Aesthetic Qualities and Transcience\", by Yuriko Saito."
    "The article started out by pointing out that everything is changing."
    # PICTURE: cycle of life?
    show lifecycle at truecenter with zoomin
    "That things were impermanent. Humans always want more."
    "There was good change, such as growth, maturation, and ripening."
    "And bad change, such as aging and deterioration."
    "Everything had various stages of good changes and bad changes, like the human life cycle."
    hide lifecycle with dissolve
    # PICTURE: messy things (laundry? untidy lawn?)
    show laundry at truecenter with zoomin
    "But change can bring about what the article called \"mess, disorder, and filth\"."
    "For example, books scattered in the office, a garden messy after coming back from vacation, an untidy toy chest after children played with the toys, or dust on a bookshelf..."
    "Saito wrote that we are always looking for the \"optimal state\" of an object."
    "We always sought to clean and to organize things."
    "Even though sometimes we are prejudiced against those who clean."
    "A common sexist notion is that cleaning is \"women's work\"."
    "Other negative notions bind the act of \"cleaning\" to those with low social status."
    "Laundry and yard work are jobs were thought to be jobs nobody wanted to do, or \"immigrant jobs\"."
    "But it turned out that we don't really care about the objects themselves when thinking about messiness."
    "Rather, we look at their location, their \"displacement\" from where it \"should be\"."
    "For example, in a fish market, it is appropriate to be loud and boisterous, and for the environment to be smelly. {w} Whereas in a library, a similar environment would be inappropriate."
    "This reminded me of the notion of the \"standard norm\" that we saw in the poem yesterday..."
    "Saito went on to argue that we don't like untidyness mainly for utilitarian reasons."
    "For example, dirty dishes, bathrooms, or clothes were unhygienic."
    "And having a dirty room made it difficult to find things."
    "But sometimes it also didn't matter. For example, having peeled paint on the walls, or cracks in the driveway, or a messy yard."
    "Saito mentioned a ridiculous incident where an 88-year-old man was arrested for not cleaning his property."
    "I didn't know that was a thing."
    "I thought it was interesting how the article mentioned that cleaning is unnatural."
    "Nature itself makes things dirty and age, yet we seek to fight against nature, in a way, by cleaning."
    hide laundry with dissolve
    "The article then talked about how messiness wasn't always a bad thing."
    # PICTURE: picturesque ideal, William Gilpin
    show picturesque at truecenter with zoomin
    "Some guy named \"William Gilpin\" was mentioned. He talked of a \"picturesque ideal\"."
    "He said that \"smoothness\" and \"neatness\" in Palladian architecture (symmetrically designed buildings) was what made it beautiful to the eye in person."
    "However, in picturesque, or, \"that of resembling a picture\", it had to be natural."
    "\"We must beat down one half of it, deface the other, and throw the mutilated members in heaps.\""
    "\"In order to make it picturesque,\" he said, \"From a smooth building, we must turn it into a rough ruin.\""
    "I guess Gilpin's point was that sometimes, the perfect picture can come from unorderliness."
    "\"Symmetric and smooth landscapes are boring,\" he continued on, \"We must turnt he lawn into a piece of broken ground, plant rugged oaks instead of flowering shrubs, break the edges of the walk, give it the rudeness of the road, mark it with wheel tracks, scatter around a few stones and bushwood, --"
    "I stopped reading. I think I got the point."
    hide picturesque with dissolve
    "I skimmed through to the last paragraph."
    "Saito concluded by saying that we shouldn't have total order nor total chaos, but a balance between the two."
    "\"We should have neither total control over inevitable natural processes nor a wholesale submission to them.\""
    "I looked up."
    "It seemed like everyone else was about done reading as well."
    "Ms. Sumner walked to the front of the room after noticing an amount of students looking up."
    show sumner normal with dissolve
    s "We usually make judgments on appearance more than anything."
    s "We judge our neighbor with the ugly lawn, the employer judges the perfect job interview candidate coming in dissheveled."
    s "In politics, candidates are judged on their hair, looks, appearance, grooming, and height, rather than their political views and goals."
    s "Another important topic is change and impermanence."
    s "Although, things don't always change for the worst. Some things age well."
    s "For example, wood, lacquerware, some pieces of artwork, ancient architecture such as ruins, and wine."
    s "It is important to find the balance between cleanliness and messiness."
    "..."
    s "Well, it looks like it is time for lunch."
    s "I will see you all tomorrow. Class dismissed."
    "I was actually looking forward to tomorrow. I was interested in what the movie version of {i}Howl{/i} would be like."
    ## lunch

label week_2_5:
    # HOWL movie
    # worksheet due next friday
    # critical response paper due next friday as well
    s "Good morning class."
    s "Today we will watch the movie Howl."
    s "You may all be thinking, \"How can a poem be made into a movie?\""
    s "Well, it turns out the movie is not exactly a word-by-word play of the poem."
    s "See, when {i}Howl{/i} was first published by Lawrence Ferlinghetti of City Lights Publisher, Ferlinghetti was arrested."
    #Dystopia
    "For some reason, I could imagine the publishing company logo."
    # PICTURE: City Lights Publisher, trial, courthouse?
    show citylights at truecenter with zoomin
    "..."
    hide citylights with dissolve
    s "This is because Howl had phrases in it that were marked obscene and non-constructive to the world of literature."
    s "This sparked an obscenity trial, where many debated over whether the poem held any social importance, or was just vulgar nonsense."
    s "The movie {i}Howl{/i} depicts this trial alongside the poem itself. Please pay attention to the parallels between the two different storylines."
    s "Additionally, focus on how the film portrays the chaos, lack of direction, and breathlessness of the poem into action."
    "Ms. Sumner set up the projector and retreated to her desk."
    # PICTURE: JAZZ
    scene bg jazz with dissolve
    "The film opened up with smooth, dark jazz playing in the background."
    play music music_howl fadeout 1.0 fadein 1.0
    "The poem was being read to an audience, but then the scene transitioned into dark, abstract images."
    "There were a bunch of naked angels everywhere. I didn't know what to think."
    "Everyone else in the class looked confused as well."
    "The angels were now eating fire and spitting it out of windows. They looked intoxicated as they flew through the skies."
    # PICTURE: COURT ROOM
    scene bg courtroom with dissolve
    "The scene then jumped to the trial that Ms. Sumner was talking about."
    p "The US Supreme Court defines obscenity as \"material which deals with sex in a manner appealing to prurient interest, utterly without redeeming social importance\"."
    "The first testifier was Gail Potter, a writer."
    "Potter" "There is no merit to this poem. I can tell from the lack of form, diction, and clarity in this poem."
    "Potter" "There is no moral greatness. And the language used in this poem is just plain crude."
    # PICTURE: GINSBERG (or person who plays him)
    scene bg ginsberg with dissolve
    "The scene then shifted to a man, I guess he was Ginsberg himself, being interviewed."
    "Ginsberg" "THere is no Beat generation... just a bunch of writers trying to get published."
    "Ginsberg then confessed how he was influenced by Jack Kerouac, the first man Ginsberg confessed his homosexuality to, to be transparent in his writing."
    # PICTURE: ghosts, skeletons, skulls chattering, subways, smoking? train?
    scene bg train with dissolve
    "The scene then transitioned once more, into more dark imagery."
    "There were subways, dark alleyways, skulls and skeletons chattering, a woman on a billboard smoking."
    "A skeleton shuddering in the dark, boxcars of a train."
    "It showed off the amount of travel done in the poem. There were skeleton-ghosts flying across the skies (I guess they were the \"visionary angels\") following a train that went throughout the country."
    "There were cars departing and leaving, and subway trains were always moving."
    "We saw an image of an angel nailed to a cross as a train travelled by in the night."
    # PICTURE: machinery, industry, rockets
    scene bg moloch with dissolve
    "The scenes were beginning to reference machinery. I think that was the \"Moloch\" in the poem."
    "The class became visibly uncomfortable as the image of phallic-shaped pine trees was displayed on the screen."
    "..."
    "For a split second, we went back to the interviewer."
    "Interviewer" "What is the difference between what you tell your muse and what you tell your friends?"
    "Ginsberg" "Absolutely nothing. It should be the same thing. Write what you are. Writing is a form of self-expression."
    "... but then we went back to the distorted images."
    # PICTURE: one-eyed shrew 
    scene bg shrew with dissolve
    "We saw the \"one-eyed shrew winking out of the womb\", and the embelical cord being ripped off forcibly."
    "The baby then crawled out and witnessed a man and women spinning in intercourse."
    show dylan thinking at right with moveinright
    d "Yo, this is weird..."
    "I agreed, and nodded in silence."
    d "Sighhh."
    hide dylan with moveoutright
    # PICTURE: dark buildings
    scene bg suicide with dissolve
    "We saw people suiciding in the night by jumping off of tall buildings."
    "We saw a homeless person injecting themselves with a drug and then turning into a skeleton and then catching fire and burning."
    "We saw the actual \"taxi cab of reality\" drie by and hit working men."
    "I guess the taxi cab, a \"machine\" of sorts, represented, again, \"Moloch\"."
    # PICTURE: COURT ROOM
    scene bg courtroom with dissolve
    "We finally returned to the court room."
    "Now some guy named Mark Schorer, an English professor from the University of California, was brought up to testify."
    "Schorer" "Yes, Howl does have literary merit."
    "Schorer" "It depicts the truth. Do you actually not believe that there are drunk people in the United States, loaded with liquor, who enjoy engaging in sexually crude activities?"
    "Schorer" "It shined light on what is currently happening."
    "The scene the transitioned back to the interview."
    # PICTURE: BROKEN DOWN APARTMENT
    scene bg ginsberg with dissolve
    "Ginsberg" "I was living in a $13/month cold-water apartmnet filled with junkies and thieves... filled with stolen silverware."
    "Ginsberg" "I was about to leave. I had had enough. As I was just leaving, I hopped into a stolen truck by accident and got arrested."
    "Ginsberg" "I had to plead insanity."
    # PICTURE: Psychiatric ward
    scene bg rockland with dissolve
    "Ginsberg" "It was in the psychiatric ward that I met Carl Solomon."
    "Ginsberg" "We talked about stuff like, is the authority of the doctors and their sense of reality right for us? Or were we the ones that were right?"
    "Ginsberg" "Carl would go through many shock treatments, but he would come out no better than he was before."
    "Ginsberg" "I finally got out of the psych ward after eight months by promising the doctor I was a heterosexual."  
    "He then talked about his mother, and how, when he was 21 years old, had to sign the paper for his mom's lobotomy."
    "His mom died at the hospital."
    "At this point, a line of the poem was read that sent shivers down my spine."
    p "Carl, while you are not safe, I am not safe..."
    "I could start seeing howl Carl's own personal sense of reality was different from the sense that society posed on him."
    "After leaving the psych ward, Ginsberg went to live with a married straight man named Neil, but then had to leave since Neil's wife caught them doing ... things."
    show dylan thinking at right with moveinright
    d "Uh."
    hide dylan with moveoutright
    "..."
    "Anyways, the scene then showed cars driving across the country into the darkness."
    p "... who drove crosscountry seventytwo hours to find out if I had a vision or you had a vision or he had a vision to find out Eternity, ..."
    # PICTURE: COURT ROOM
    scene bg courtroom with dissolve
    "And then again, we were back at the obscenity trial."
    "The testifier this time was Luther Nichols, a literary critic from the San Francisco Examiner."
    "Nichols" "Yes, {i}Howl{/i} has literary merit."
    "Nichols" "There was a lack of inhibition in those in the post-World War II generation."
    "Nichols" "I believe that this poem can surely withstand the trials of time."
    "And then we cycled back to the interview."
    "Ginsberg" "Poetry is a rhythmic articulation of feeling. You can feel the impulse."
    "Ginsberg" "When first writing Howl, I didn't know what it meant. But maybe after two years, it would come to me clearly."
    "Ginsberg" "I would say my work is like a photograph developing slowly."
    "Ginsberg" "My psychiatrist, Dr. Hicks, asked me one day after I went to California: \"What do you want to do?\""
    "Ginsberg" "I told him I wanted to write. He said, \"Then do it.\""
    "Ginsberg" "So I quit my job and went full-time writing."
    # PICTURE: tall building breathing fire? moloch - devil-like beast with horns
    scene bg molochred with dissolve
    "The poem was now at the part where \"Moloch\" was being repeated over and over."
    p "Moloch whose eyes were a thousand blind windows..."
    "There was a tall building with a face, breathing fire. Inside the mouth was a devil-like beast with horns."
    scene bg sacrifice with dissolve
    "The citizens of the town were sacrificing their children to Moloch in the fire to be rewarded with a gun and a worksuit. They then became machines."
    # PICTURE: destruction and ruin of a city
    scene bg molochgreen with dissolve
    "In the end, the citizen-machines died and their skulls were collected. The city lights on fire due to the massive amount of machines."
    "All the buildings gave off billows of smoke and pollution, and tanks and cars populated the town."
    # PICTURE: COURT ROOM
    scene bg courtroom with dissolve
    "Once more, we were taken back to the trial."
    "The person speaking this time was David Kirk, an English professor from the University of San Francisco."
    "Kirk" "This poem has no literary merit. It has no form. If it has a form, it's a weak imitation of a form... namely, Walt Whitman's form."
    "Kirk" "The theme, or idea, is clear, but it has a negative value. Therefore, this poem holds no validity."
    "Kirk" "It merely celebrates the unfortunate life of Solomon, a drifter of Dadaist persuasion."
    # PICTURE: shock treatment
    scene bg rockland with dissolve
    "We returned then, to the obscene imagery."
    "This cycling was starting to drive me in circles myself."
    p "I'm with you in Rockland, where you're madder than I am."
    p "... where you're the shade of my mother..."
    "We saw a woman being wheeled down a hospital hallway, screaming."
    "We saw a man, presumably Solomon, receiving shock treatment."
    # PICTURE: angels vs machines and Moloch; bombs/bibles on buildings
    scene bg molochlight with dissolve
    "Back in the city, the flying angels meet the machinery and Moloch."
    "They drop \"bombs\" (more like bibles or books) on the buildings and destroyed them."
    "It looks like the angels were the good guys after all? I couldn't really tell."
    "But they beat Moloch eventually."
    p "... the hospitals illuminate themselves..."
    p "... the war is here..."
    p "... where you walk to my cottage in the western night..."
    "The reader kept reading the poem, and we were nearing the end."
    "Finally, we went back to trial. From the tone, I guessed that this would be the last scene that we saw."
    # PICTURE: COURT HOUSE
    scene bg courtroom with dissolve
    "They began talking about what the poem would sound like to the \"average\" reader."
    "The man in the black suit, who I guess was the defense for the defendant, stood up and began giving a lengthy speech."
    "Man" "We want to censor and defend our own wellbeing."
    "Man" "People who censor do not feel their own physical or moral health are in jeopardy."
    "Man" "We want to impose our thoughts onto others. Do we truly want everyone to have a liberal education, or do we really want to add fuel to the fire of ignorance?"
    "Man" "The desire to make the world conform to our own views... it will take a long time to battle this human desire."
    "Man" "Let there be honesty! Let there be light!"
    "Man" "{i}Howl{/i} calls attention to what is visible, but unseen... it changes men's minds."
    "Man" "No two persons think alike. An author should be able to use his own words - there should be no euphemisms!"
    "Man" "Freedom of speech and press are inherent in a free nation."
    "And with that, it looked like the judge was convinced that the poem really did have redeeming and social importance."
    "We went back to the interview for a split moment (so I guess I was wrong when I assumed that the transition to the court room would be the last transition...)"
    "Ginsberg talked about how his poem reflected the basic reality of homosexual joy."
    "Ginsberg" "It is not a promotion of homosexuality. It is a promotion of frankness. And I think that being frank is socially useful."
    p "Holy, holy, holy holy ..."
    p "Everything is holy."
    p "The bum and the seraphim are holy."
    p "Holy is the angel in Moloch."
    p "Holy he abyss, holy forgiveness, holy charity..."
    "I guess this was part of the poem. It must have been that fourth part that wasn't in our printout when Ms. Sumner read it to us."
    "After the presenter was done reading the poem, the movie drew to a close."
    scene bg class_day with dissolve
    play music music_class fadeout 1.0 fadein 1.0
    show sumner normal at center with moveinleft
    "The class was quiet as Ms. Sumner walked to the front of the room and shut off the projector."
    s "So. We can see multiple storylines in this movie, from the actual poem itself, to the interview, to the proceedings in the court house."
    s "I will now pass around a worksheet. Please fill this out and hand it in by next Friday."
    "Ms. Sumner gave the student in the front of the class a stack of papers, which was then passed around."
    s "Additionally, I will be assigning you a second essay. Write about the following topic: How does the film aestheticize the poem, its author, and the historical context and trial?"
    "Oh boy. Another essay."
    "I planned on starting this one early, so that I wouldn't have a repeat of last time."
    "I certainly did not want to rely on Aura for the ideas for all of my essays."
    "Once everyone got the handout, Ms. Sumner dismissed the class for lunch."
    s "I will see you all after the weekend. We will being a new topic next week, where we focus on the human senses."
    
    
label weekend_2:
    # weekend of week 2
    # work on Worksheet and critical response?
    
label week_3_1: 
    #"The Senses In Play"
    # Video 1: Synesthesia: A Film by Jonathan Fowler
    # Video 2: TEDxCareltonU 2010: Jim Davies - The Science of Imagination
    show sumner normal at center with dissolve
    s "Good morning, everybody."
    s "As I mentioned last week, the new topic we will be focusing on this week is regarding the human senses and perception."
    s "As is custom with introducing new material, we will watch two clips."
    "Of course."
    "Ms. Sumner set up the projector like always and stepped back to her desk as the film began rolling."
    hide sumner with moveoutleft
    "The first video was about something called \"Synesthesia\"."
    # PICTURE: something to do with synesthesia
    show synesthesia at truecenter with zoomin
    "The title of the clip was \"Synesthesia: A Film by Jonathan Fowler\"."
    "They defined synesthesia as \"a sensation produced in modality when a stimulus is applied to anothe modality.\""
    "It was a cross-sensory percetion, and those with synesthesia were called synesthetes."
    "It was an alternate way of perceiving the world."
    p "For example, synesthetes can experience a \"taste of the feeling\", or the \"smell of the numbers\", or see the \"color of the letters\"."
    p "It is a very important force for imagination."
    p "Just because you can't see something with your eyes doesn't mean it doesn't exist."
    "That is true."
    "I remember back in middle school, whenever I studied for a test I would associate foreign terms or concepts with things I was comfortable with."
    "I think they called those mnemonic devices or something."
    hide synesthesia with dissolve
    "..."
    "The second video then started playing."
    # PICTURE: TED talk (imagination?)
    show imagine at truecenter with zoomin
    "It was a TED talk by Jim Davies, on the topic of the \"Science of Imagination\"."
    "Davies" "An important human ability is that we have the power to reason hypothetically. In a sense, we can predict the future."
    "Davies" "Our imagination is constrained by our environment, what we know, and our visual memory."
    # PICTURE: imagination machine
    "A machine was presented on the screen that could \"imagine\" things. It was called Visuo."
    "The computer vision, or object recognition, software automated imagination and displayed boxes with heights and numerical values."
    "There was something called an Image Oracle too, which displayed something in its \"imagination\" with a certain percentage chance."
    "I thought it was pretty cool, actually."
    "Davies" "Imagination doesn't come out of nowhere. Everything you have ever imagined has a firm base in reality."
    "Davies" "We tweak reality in interesting ways to make an interesting or entertaining world."
    # show aura normal at right with moveinright -- a "Just like this visual novel." "... what was that?" -- 4th wall
    "I think Davies' point was that imagination isn't original. It was kind of a bleak way of thinking of things."
    "Davies" "It takes a good understanding of reality to make a compelling fantasy."
    "..."
    hide imagine with dissolve
    "The talk ended."
    show sumner normal at center with dissolve
    s "I hope you enjoyed the intro."
    s "This week, we will learn how we use our human senses to perceive art, and the nature behind human imagination."
    s "Class dismissed."
    ## lunch
    
label week_3_2:
    # "Performance" by Paul Bloom
    s "Good morning class."
    s "These next two days, we will be reading two articles by Paul Bloom, a psychologist."
    s "Today, we will begin with the article \"Performance\"."
    "A stack of papers was passed around."
    "When the stack came to me, I grabbed a handout and passed it to my right."
    "I looked down at the first page."
    "\"Performance\", by Paul Bloom."
    "I began to read."
    # PICTURE: groupthink
    show groupthink at truecenter with zoomin
    "The article began by arguing that humans are swayed by groupthink - that they can't appreciate beauty or talent without being told what it is."
    "According to Arthur Koestler, a journalist, humans are weak, snobs, and intellectually lazy."
    "They gave the example of Joshua Bell, a famous violinist, who played in a subway in New York for about 45 minutes, yet went unnoticed."
    "They gave another example of a Picasso Painting owned by a woman named Catherine, who thought that the painting wasn't worth a second glance until she found out it was actually painted by Picasso."
    "They then finished with a third example of a Dutch forger named Han van Meegeren who painted Vermeers just as good as the original."
    "In all three cases, the artists used the \"same paint\", the \"same sequence of notes\", but just a \"different frame\"."
    "It turns out that people's tastes in music are strongly dictated by their social groups."
    "\"Familiarity breeds pleasure\", they say - we like what we've heard before."
    "Even if we know what we see isn't what it really is, we still trust our eyes."
    "For example, cutting up pictures of our wedding rings, eating fudge that looks like poop, or throwing darts at pictures of babies are all harmless things..."
    "... but we are very against doing them because of the related objects' outward appearance."
    "We enjoy art because it tells us information about others - in particular, the painter."
    "We prefer originals because of the history behind the artwork."
    "The original painting was \"in touch\" with the artist."
    "Even with the advent of machining reproduction, we still favor \"the original\"."
    "The original ties back to the artist, and contains a residue of the creator, or the user."
    "The article then gave some more examples of art tying back to the creator, such as Aliza Shvarts producing a series of self-induced miscarriages."
    "I stopped reading after the paragraph about the artist that made 91 cans of feces, one of which was sold for $61,000."
    hide groupthink with dissolve
    "... I waited a while and then looked up."
    "It looked like everyone else was finished reading as well."
    "Ms. Sumner stood up and began speaking."
    show sumner normal at center with dissolve
    s "A lot of great artists' works were shown to go unnoticed."
    s "Many people do not appreciate talent, mainly because of the \"frame\" it is presented in."
    s "Humans by nature are shallow, and do not want to spend the time to investigate further, beyond the \"frame\"."
    s "As you go about your daily lives, try to reason more deeply; try to look beyond the frames, so you can spot true beauty."
    "Learning about artists all of a sudden became a life lesson."
    s "That is all. Tomorrow we will read the second of Bloom's articles. Class dismissed."
    hide sumner with dissolve

label week_3_3:
    # "Imagination" by Paul Bloom
    show sumner normal at center with dissolve
    s "Good morning, class."
    s "Today, we will read the second article by Bloom."
    "The papers were passed around just like yesterday."
    s "Although written by the same author, this paper deals with a different topic - that of imagination."
    hide sumner with dissolve
    "I looked down at the handout in front of me."
    "It literally said \"Imagination\" at the top."
    "I began to read."
    "..."
    "As I got further along, I figured that the main idea was that we don't distinguish imaginitive experiences from real ones."
    # PICTURE: television/novels/books/video games
    show tv at truecenter with zoomin
    "I read that most of our leisure time is spent participating in experiences we know are not real, such as books, movies, video games, TV, or ficticious worlds we create."
    "I realized that was actually true..."
    "The article continued: two year olds pretend to be lions, graduate students stay up all night playing video games, young parents read novels, etc..."
    "Although children play pretend, they know the difference between real life and pretend."
    "We even saw pretending in nature. For example, dogs play-fight. They practice skills beneficial to survival."
    "The article then shifted to talk about another topic: metarepresentation."
    "This gives humans the power to reason about false beliefs."
    "Humans were different from animals in that they could predict what others were thinking."
    "... metarepresentation also allows us to lie, to put false ideas into others' heads."
    "I remember in my elementary school days when we would sometimes drag out and playfully say the phrase \"I know that you know that I know that you know that I know that you know that ...\""
    "I think that type of recursive reasoning was what they were getting at in the article."
    "Or some confusing phrase like \"They don't know that we know that they know we know!\" which actually isn't that confusing once you think about it for a while."
    "..."
    hide tv with dissolve
    "I finished up the rest of the article."
    show sumner normal with dissolve
    s "On the topic of imagination and false realities..."
    s "The reason why we enjoy these fictitious worlds is because we are moved by the stories, by characters and events we know don't exist."
    s "The imagination may be fake, but the emotions we feel are very real."
    s "We are finished for today. Enjoy your lunches. Class dismissed."
    hide sumner with dissolve
    
label week_3_4:
    # "Aesthetics, Neuroaesthetics, and the Sister Arts" - G. Gabrielle Starr
    # assignment: compare the 2 readings. due next friday.
    show sumner normal at center with dissolve
    s "Good morning everyone."
    s "We covered aesthetics in the first week, but we will take a brief trip back to that topic today with the article we will read."
    "Copies of the article were passed around to each student."
    s "Please give it a read."
    hide sumner with dissolve
    "I looked down at the article on my desk. This one seemed like a stack of papers in itself."
    "I picked it up to make sure I didn't grab more than one."
    "Nope. It's just a super long article."
    "\"Aesthetics, Neuroaesthetics, and the Sister Arts\", by G. Gabrielle Starr."
    "I opened up the first of many pages of the article."
    "The three sister arts, according to Starr, were music, painting, and poetry."
    "I couldn't quite follow the philosophical talk about imagination and imagery having to do with Plato's images."
    "But I found it interesting that Starr wrote how artists such as poets and painters were \"peddlers of falsity\"."
    "This reminded me of the first week's video, where we learned that Plato thought of artists as copycats, or copiers of reality."
    "I skimmed through a few paragraphs until I found a word I was familiar with: somaesthetics."
    "We feel the emotions in our bodies when we read tragedy. We have a quickened heartbeat when we read something frightening, or the scene holds a lot of tension."
    "I think she was getting at how we react with our bodies, even when entertaining an imaginary world."
    "The article then got extremely technical, talking about a \"neuroaesthetic model\"."
    "Starr attributed the emotion reaction we give to art to the \"circuits in the brain that represent, evaluate, compare, and deliver award\"."
    "I thought this had a lot to do with that Shusterman guy's somaesthetics."
    "..."
    "I couldn't quite follow the rest of the article, so I just skimmed through to the end."
    "I kept at it until Ms. Sumner's voice interrupted my skimming."
    show sumner normal at center with dissolve
    s "I know this is a long article, and a lot of you are not finished reading."
    "\"A lot of you?\" I would be surprised if anyone here even got halfway through."
    s "But it is almost time for class to be over. Please finish up the article tonight."
    "I probably wouldn't finish reading it tonight."
    "I didn't understand most of it, anyway."
    s "Additionally, do not forget that both the {i}Howl{/i} worksheet and essay are due tomorrow."
    s "I will see you all then. Class dismissed."
    hide sumner with dissolve
    "I had already finished the worksheet and essay over the weekend."
    
label week_3_5:
    # "Against the Grain" and "Tender Buttons"
    # assignment: picture essay. due next friday.
    "I handed in the worksheet and essay as I walked in."
    show sumner normal at center with dissolve
    s "Good morning."
    s "The reading we do today will not be as intensive as yesterday."
    "The reading was passed around."
    "It looked like two stories."
    "The first was \"Against The Grain\", by someone nmed Huysmans."
    "The second was \"Tender Buttons\", by Gertrude Stein."
    s "For the second piece, Tender Buttons, just read the section \"Food\"."
    hide sumner with dissolve
    "I began reading the first one."
    "..."
    "It didn't make any sense."
    "It had no plot at all."
    "What was the point of this story?"
    "..."
    "The main character, Jean, seemed like a strange and terrible person."
    "I skimmed through since I couldn't quite follow the plot."
    # PICTURE: turtle with gem shells (shiny shell?)
    show turtle at truecenter with zoomin
    "All I know is that at one point, he bought a turtle and shoved gems into its shell to turn it into a living jewel."
    "... and then the turtle died."
    "I moved on to the next... poem, I suppose."
    "I flipped to the section on Food."
    hide turtle with dissolve
    # PICTURE: from photoessay
    scene bg buttons1 with dissolve
    "... similar to the last thing I read, there was no story at all."
    "It was more like a play on words, with multiple run-on sentences."
    "Was this even poetry?"
    "I guess if someone read this out loud, it would sound kind of cool."
    "... \"tender and changing and external and central and surrounded and singular and simple and the same and the surface and the circle and the shine and the succor and the white and the same ...\""
    "... \" and the better and the red and the same and the centre and the yellow and the tender and the better, and altogether.\""
    "Whaaaaaaat?"
    "I was lost."
    "The words and sentences stopped making sense. Were they even sentences?"
    "I read through the entire thing, not retaining any information at all."
    scene bg class_day with dissolve
    show sumner normal at center with dissolve
    s "These two works of literature don't really have much meaning to them in regards to plot."
    "I could see that."
    s "But what they do have is brilliant imagery."
    "... I suppose."
    s "The next assignment is to construct a photo essay based on one of these readings."
    s "Focus on what the text makes you see, what it makes you feel... what it makes you {i}imagine{/i}."
    "Ah. I should have known, could have guessed, that that was the point of having us read these two senseless works. Since this week's focus was on imagination, after all."
    s "A photo essay is a series of photographs that tell a story, or evoke feelings in whoever is \"reading\" it."
    s "You may accompany your essay with captions. This will be due a week from today."
    "A photo essay? I had never done one of those before."
    "Surprisingly, I was actually looking forward to it."
    s "That will be all for today. Class dismissed."
    hide sumner with dissolve
    
label weekend_3:
    # compare/contrast?
    # picture essay."
    "I couldn't think of anything to put in my photo essay."
    "I decided I would do one based on the second piece we read, \"Tender Buttons\"."
    
label week_4_1:
    #Mod 4: Into The Digital Dimension
    #"How to Read a Digital Text"
    # Virginia Woolf's "The Waves"
    #assignment: interpret Wolf's "The Waves" using digital media: MC will use a photo essay...
    show sumner normal at center with dissolve
    s "Good morning everyone. I hope you all had a wonderful weekend."
    s "This week we will focus on works of art in the digital dimension."
    s "Today we will be reading the first part of a short story and then listening to it."
    "The relevant papers were passed out to the students."
    "I looked down and read the title on the paper."
    "\"The Waves\" by Virginia Woolf."
    s "Please give it a read, and pay attention to the imagery. We will listen to a reading of it afterwards."
    hide sumner with dissolve
    "It didn't seem that long. Then again, it was probably just a short section out of a huge work of literature."
    "I began to read."
    # PICTURE: WAVES / RISING SUN
    "\"The sun had not yet risen...\"."
    "There definitely was a lot of imagery. Especially of light and dark."
    "I could imagine a sun rising on the horizon of the ocean, with waves crashing against the shore, and birds chirping on the roof of a beach house."
    "I finished reading and looked up."
    show sumner normal at center with dissolve
    s "We will now listen to an audio recording of the reading."
    "Ms. Sumner began playing back the tape on which the voice was recorded."
    "The reader's voice seemed a bit melancholic."
    p "Gradually the dark bar on the horizon had become clear as if the sediment in an old wine-bottle had sunk..."
    p "... and the air seemed to become fibrous and to tear away from the green surface flickering and flaming in red and yellow fibres like the smoky fire that roars from a bonfire..."
    "I could definitely picture the scene better when it was read to me."
    "..."
    "And finally, the recording was over."
    s "You may have noticed that new images popped up in your mind in the audio version, images that did not appear when you were reading it on your own."
    s "Last week we covered the senses. Hearing is one of these senses."
    s "Using your sense of hearing to interpret a work of literature can have a different impact as opposed to just reading it."
    s "For your next assignment, interpret Woolf's \"The Waves\" using some form of digital media."
    s "It can be a movie, a digital recording, a slide show, or some other form of media."
    s "Please email me the relevant files by next week. It will be due one week from today."
    s "That will be all. Class dismissed."
    hide sumner with dissolve

label week_4_2:
    # "Embodied Visions: What Does it Mean to Look At a Work of Art?" - Siri Hustvedt
    # part 1
    show sumner normal at center with dissolve
    s "Good morning, class. We will continue this week exploring the effects digital media has on art."
    s "Today and tomorrow we will be reading an article by an essayist and journalist, Siri Hustvedt."
    "A stack of papers was passed around the room as each student took one."
    "When the stack came to me, I grabbed a handout from the top and passed the rest to my right."
    "I took a glance at the first page."
    "\"Embodied Visions: What Does it Mean to Look At a Work of Art?\" by Siri Hustvedt."
    s "As you read, consider the medium in which you experience art; does the medium matter?"
    hide sumner with dissolve
    "I began to read the article."
    "..."
    "It started out by describing how we enjoy art due to the human faculty of a \"reflective self-consciousness\"."
    "As we grow, we become self-knowing and self-aware, something that separates us from the other animals."
    # PICTURE: human facial expression/mimicry/mimes?
    "Human infants mimic others' facial expressions as they grow up. This occurs even before self-recognition in a mirror."
    "Facial expressions are important in that they affect thoughts, memories, and feelings."
    "We grow through others."
    "..."
    "Humans are driven to be artists even though it does not have anything to do with survival or utility at all."
    "The article then talked the notion of something called \"intentionality\" in art. Intentionality was described as a \"reference towards content\", or a \"direction towards an object\"."
    "I thought of it as a form of communication."
    "The article reaffirmed my hypothesis by continuing, that art establishes a relationship between the viewer, or reader, or listener, and the artist."
    "Humans understand symbols better than words. We have to learn how to read and speak, but we can look at faces on people and tell immediately how they feel without having them tell us."
    # PICTURE: enslavement, torture, death, mental institution
    "We were then given an example of this \"communication of feelings\"."
    "An artist by the name of Henry Darger experienced his parents' deaths and was sent to a mental institution."
    "His art work was reflective of his experiences. The article described his art as an \"epic of children enslaved by sadistic adults, a narrative of suffering and insurrection that finally ends in triumph.\""
    "..."
    "The article then talked about how humans have an unconscious \"proprioceptive\" sense."
    "That is, we had the ability to sense position, orientation, and movements with our body parts in space."
    "This seemed like a lot to do with Shusterman's somaesthetics again..."
    "Anyways, our sensitivity to art is personal, and a viewer's reaction to art depends on the person or viewer."
    # PICTURE: colors of rainbow?
    "We \"feel\" green, or blue, or red, before we can even name the color."
    "This part reminded me of the week we learned about synesthesia."
    "We respond bodily to an object's perceived meaning according to past experience before we even identify the object."
    "..."
    "I had gotten about halfway through the article, when I heard Ms. Sumner's voice."
    show sumner normal at center with dissolve
    s "That will be it for today. We will continue reading this article tomorrow."
    s "Enjoy your lunch time. Class dismissed."
    hide sumner with dissolve

label week_4_3:
    # Embodied Visions/Siri Hustvedt part 2
    show sumner normal at center with dissolve
    s "Good morning, class."
    s "We will continue reading Hustvedt's article today."
    s "Please continue reading where you left off of yesterday."
    hide sumner with dissolve
    "I pulled the article out of my bag and laid it on my desk."
    "I flipped through the pages until I found the point where I left off yesterday."
    "... where was it.... ah, unconscious proprioceptive sense. No, that wasn't it. It was something about feeling colors."
    "I finally found the spot, and began reading again."
    "... humans are inductive by nature."
    "\"When the brain receives a new sensory input from the world in the present, it generates a hypothesis based on what it knows from the past to guide recognition and action in the immediate future.\""
    # PICTURE: shiny glob of spit or shiny blue stone on ground
    "Hustvedt then gave an example of how her husband picked up what he thought to be a shiny blue stone, only for it to turn out to be a shiny glob of human spit."
    "I guess that was a real example of \"using past knowledge to predict the immediate future\"..."
    "Anyways, we engage in perceptual learning: we have expectation, and orientation."
    "For example, a blind person suddenly obtaining vision cannot use it well due to lack of experience."
    "..."
    # PICTURE: mirrors
    "We mirror what we see in our minds. We mirror the world in our brains."
    "Hustvedt reflected her viewing of a fruit painting."
    "\"They are fictions in a fictitious world, an imaginary elsewhere that has opened up before our eyes...\""
    "The article then began to talk about imaginitive play."
    "This reminded me of Paul Bloom's article on imagination."
    "Anyways, humans begin playing \"pretend\" at the age of three."
    "We have the ability to \"remember ourselves in the past and project ourselves into the future\"."
    # This line is important. Will be in the finale, definitely. (About Aura - the imaginary space.)
    "In a sense, humans can be in two places at once. The real world is one. And then another is the imaginary space that exists side by side with real space."
    "The body is available not only in real situations into which it is drawn, but it can also turn aside from the world, lend itself to experimentation..."
    "The body can take its place in the realm of potential. In this realm of potential, art happens. In this fictional space, that we pretend exists, art happens."
    "... and the article ended with that."
    "This was actually a pretty amazing article."
    "I looked up, and it seemed like the majority of the class was finished as well."
    "Ms. Sumner stood up and began speaking."
    show sumner normal at center with dissolve
    s "Humans can reason under uncertainty. We have a nondeterministic way of thinking."
    s "The fact that we can entertain multiple possibilities, multiple theoretical futures - this is in essense \"human free will\"."
    s "We have the power to predict and plan ahead based on experience."
    "I did feel sometimes like I was living in two worlds. One inside my head, and one in reality. But it always felt like the same reality. Was there really a difference?"
    "I began to think deep thoughts."
    s "That will be all for today. Class dismissed."
    "However, my hunger swept aside those thoughts, and all I could think about now was food."
    hide sumner with dissolve
    "I began to head out to lunch."

label week_4_4:
    # examples of Digital Media: the Alice visual novel?
    # from Electronic Literature collection
    show sumner normal at center with dissolve
    s "Good morning."
    s "Today we will take a look at an example of digital media."
    s "We will be playing through what is known as a \"visual novel\"."
    s "Usually, visual novels are like a kind of choose-your-own adventure book, but with graphics, sound, and sometimes voices."
    s "But the one we will play through today is known as a \"kinetic novel\". That is, there is only one linear storyline, and the choices, if any, do not have any affect on the storyline."
    "A visual novel? I had always been a fan of comics as a kid. I wonder if it was like that?"
    "Oh wait, I remember the choose-your-own adventure kind of books as well. I would always flip back and forth through all the pages and try to get every ending."
    "I was actually pretty excited for this."
    "Ms. Sumner set up the projector, but this time instead of a clip being played, it looked like a title screen."
    # PICTURE: Destiny Loop visual novel (make it yourself and take screenshot) - VN-ception!
    "The name of the visual novel was \"Destiny Loop\", and there were buttons for \"Start Game\", \"Load Game\", etc."
    "..."
    "The story started out with the main character being a normal college student attending classes like normal."
    "... but then it looked like weird creatures began to invade the city or something."
    "The main character and his friends were travelling around, trying to find shelter from these atrocities."
    "After a series of events, the one of the main character's friends had died."
    "I could almost feel the main character's pain. At this point, the tension in the air was so thick, you could probably cut through it with a knife."
    "The entire class was on the edge of their seats."
    show dylan normal at right with moveinright
    d "Oooohhhhhhhhhh!"
    "... even Dylan seemed to be interested. That didn't happen very often."
    hide dylan with moveoutright
    "..."
    "Eventually only the main character was left, and all of his friends had been killed off one by one."
    "But in the end, the main character travelled back through time and saved his friends."
    "However, the main character was stuck in the past and had to live through everything again, while his friends, now alive, were sent to the \"future\", and lived on without knowing anything about the invasion."
    "It was a very bittersweet ending."
    "It left me wanting more."
    "I'm sure everyone in the class felt the same way."
    "The project was shut off by Ms. Sumner."
    show sumner normal at center with dissolve
    s "I am sure many of you felt strongly about this visual novel."
    s "What different would it have made if the story were presented through an actual novel instead? Or as a short story?"
    s "In your next assignment, please write an essay regarding the topic of whether the medium in which art is presented through actually matters."
    s "Analyze the visual novel as an example of literature in the digital realm. Try to relate it to Hustvedt's article."
    s "This will be due next Friday."
    s "That will be all for today. Class dismissed."
    hide sumner with dissolve

label week_4_5:
    # critical response paper: on some digital media. relate to siri hustvedt. due next friday on week 5.
    show sumner normal at center with dissolve
    s "Good morning, everybody."
    s "We are a bit ahead of schedule today, so I will let this class be a free study hall."
    s "You are free to work on whatever work you have. I suggest working on the essay."
    hide sumner with dissolve
    "Ms. Sumner retreated to her desk after making the announcement."
    "I decided to work on the essay."
    "I wrote about how there was a bunch of foreshadowing in the plot of the visual novel."
    "There was also the literary device of irony. It was ironic that the main character went back to save his friends, yet he himself wasn't \"saved\" in the end."

label weekend_4:
    # weekend after week 4. perhaps work on critical response
    "I finished up the essay. My main argument was that the medium in which art was presented didn't really matter."
    "I wrote about how there was no need to actually identify art in the media; rather, we just had to feel it. There was no need to give it a name."
    "The \"frame\" in which it was presented in didn't matter, as long as the feelings got through."

label week_5_1:
    # Mod 5: What is Creativity?
    # Elizabeth Gilbert's TEDx Talk (eat pray love)
    show sumner normal at center with dissolve
    s "Good morning everybody. I hope you all had a wonderful weekend."
    s "This week we will be focusing on the topic of creativity."
    s "What is creativity? How do we become creative? How does one fail at being creative?"
    s "These are all questions we will explore this week."
    s "As always, we will begin with an introductory video."
    "Ms. Sumner set up the projector as a film flickered onto the screen."
    hide sumner with dissolve
    "It was a TED talk by Elizabeth Gilbert."
    "Apparently she had published a book called \"Eat Pray Love\" that was very popular."
    # PICTURE: Eat Pray Love
    "Gilbert" "After writing the book and seeing its success, I struggled to write the next book."
    "Gilbert" "The next book wouldn't be Eat Pray Love."
    "Gilbert" "The people who liked it wouldn't like it. The people who didn't like it still wouldn't like it."
    "Gilbert" "I was paralyzed by this fear of failure, that I didn't get anything done."
    "Gilbert" "After I came out of college, I spent six years trying to get published as a diner waitress."
    "Gilbert" "I wanted to \"quit while I was behind\", and was very close to giving up."
    "Gilbert" "But, I loved writing more than I hated failing at writing."
    "Gilbert" "Which meant that I loved writing more than I loved my own ego."
    "Gilbert" "Which meant that I loved writing more than I loved myself."
    "Gilbert" "So, I kept persisting."
    "She then talked about the notion of \"two extremes\"."
    "Gilbert" "Failure puts you in the blinding darkness of disappointment. Success catapults you all the way to the equally blinding glare of fame, recognition, and praise."
    "Gilbert" "If you are ever displaced, you need to find your way back home from these two extremes."
    "Gilbert" "Your home is what ever in this world you love more than yourself."
    "Gilbert" "Your home is that thing to which you can dedicate your energies with such singular devotion that the ultimate results become inconsequential."
    "... did I have something like that? It sounded like a very idealistic concept."
    "Gilbert" "So I just kept writing. Many of my books will fail, some might succeed."
    "Gilbert" "But I will always be safe from the random hurricanes of outcome. You just have to find the best, worthiest thing that you love most, and build your house right on top of it."
    "Gilbert" "If you should some day, somehow, get vaulted from your home either by great failure or great success, work your best to find your way back home."
    "... and with that, the talk was over."
    show sumner normal with dissolve
    s "When I first went into the field of education, it was very difficult to get a job. My friends at the time would sometimes poke fun at me."
    "This was strange. It was not like Ms. Sumner to get all personal."
    s "But, I realized that what I loved to do most was teach."
    "... even though she barely taught and just sat behind the desk all day while we watched videos or read."
    s "And so I kept persisting and now, I have come to this job that I love."
    "I would love just playing movies for a classand handing out readings every day as I just sit behind my desk as well."
    s "Anyways, the point is, is that you should do what you love over and over again, disregarding succes and failure."
    s "This is what leads to creativity. Tomorrow we will watch another presentation on creativity, but this will be all for today."
    s "Class dismissed."
    hide sumner with dissolve

label week_5_2:
    # How to Be Creative (PBS)
    show sumner normal at center with dissolve
    s "Good morning, class."
    s "We will watch one more presentation today, continuing the introduction to this unit on creativity."
    "The project was set up, and the film began displaying on the screen."
    "It was a PBS broadcast titled \"How to be Creative\"."
    "Wasn't this a kid's show?"
    "Anyways, the presenter began speaking."
    p "Creativity is a process. First, you must ask yourself, \"How do I do this?\""
    p "You must expand your capacity for uncertainty."
    # PICTURE: binary search tree/decision tree that represents paths you can take
    p "We must be in a state of \"negative capability\" - that is, the space where we don't know what's going to happen next."
    p "We must chase down ideas, and understand that not all of them are going to lead somewhere."
    p "However, even if an idea leads to a dead end, it was not a waste of time. This is because the experience of pursuing and idea will influence the next one."
    p "Creativity is a process of excitement and despair - you just have to keep at it."
    p "As Chuck Close once said, \"Inspiration is for amateurs. The rest of us just get up and go to work.\""
    # PICTURE: the brain and creativity?
    "The presentation then moved to discuss the cognitive stages of creativity."
    p "The first stage is preparation."
    p "In this stage, we must learn a lot of things. We must learn the underlying structure of what we are trying to create, all the nitty-gritty stuff."
    p "In this stage there is not much creativity going on, but it is necessary for the whole."
    p "The second stage is incubation."
    p "In the incubation stage, we just need to \"let it go\". We need to wander away from the current task, to let our minds rest."
    p "The majority of our ideas come from our subconscious, a force much more intelligent and powerful than we are."
    p "So we must rely on that until the third stage, which is illumination."
    p "This is the stage of \"insight\", where the connections subconsciously collide and reach the threshold of consciousness."
    p "It is that \"Aha!\" moment in the creative process."
    p "And finally, we have the verification stage."
    p "In this stage, we use our critical thinking skills to think about the audience, to craft the message and to make it best received by people."
    p "We need to package it just the right way. The best works of art can go unnoticed if packaged the wrong way, or if the presentation isn't the best it could be."
    "That was some very technical stuff."
    "I didn't think that those four stages crossed anyone's minds when they were painting or playing an instrument."
    "The presentation then transitioned to a different subject."
    # PICTURE: working together
    p "We must transcend the idea of \"the lone creator\"."
    p "Creativity needs healthy collaboration."
    p "A group of artists working together forms a type of \"meta-artist\", whose skill is the sum of all skills of a creative group."
    p "However, everyone in the group needs to have a certain level of creative maturity. That is, a person's idea is not the person him- or herself."
    p "Criticism of an idea are not criticisms of the person who holds that idea."
    p "In a group, you can't be married to your ideas. You need to be able to let go of them as well in order to learn to work with different people, who hold different ideas."
    "I wasn't too sure about the skill being the \"sum\" of everyone's skills in a group part."
    "From my experience, whenever I worked in a group project, everyone tended to work less than they would if they were to work alone, since everyone believed that the work would be divided up amongst the members of the group."
    "As a result, the \"total skill level\" was probably half of the sum of everyone's skill level."
    "Though, if a group of people formed and everyone in the group loved what they did, I guess I could see their creative skill being the sum of everybody's."
    "The PBS broadcast then went on to talk about originality."
    # PICTURE: originality? the chicken vs the egg
    p "Nothing is original. Ideas don't just come up out of the blue."
    p "Influence comes from somewhere, or some one else."
    p "We take other people's work, and copy it, or transform it, or combine multiple works to create something that is called \"original\"."
    p "In a sense, it is not really \"original\". We are merely performing mimicry, or making variations of a platform that already exists, or make existing ideas harmonize."
    p "For example, Gutenberg's invention, the printing press, was a mix of many different technologies."
    "..."
    "The broadcast ended with some more examples of creativity that were not really that original."
    show sumner normal at center with dissolve
    s "The ideas that you have are just things you have already known, but synthesized to become something new."
    s "Anyone can be creative in the domain that is best for them to express themselves."
    "The domain that is best for them to express themselves, huh? I wonder what that \"domain\" was for me..."
    "As I pondered this, Ms. Sumner began to dismiss the class."
    s "That will be all for today. Enjoy your lunches."
    hide sumner with dissolve
    
    
label week_5_3:
    # "Creativity in the Post-Google Generation" by Edwards
    show sumner normal at center with dissolve
    s "Good morning, class."
    s "Today, we will read an article about creativity in an emerging world of technology."
    "An article was passed around to each student."
    "I read the title: \"Creativity in the Post-Google Generation\", by David Edwards."
    "I began to read."
    hide sumner with dissolve
    "Edwards talked about artscientists as idea translators, and the five steps involved in the process."
    # PICTURE: creative process
    "First, they passionately profess their idea and their goals."
    "Then they study relevent topics pertaining to their ideas, and open themselves up to new experiences."
    "Third, they struggle through peer critique, alongside audience critique."
    "Fourth, they keep trying new things, testing these things against the critiques of peers and audiences."
    "And lastly, while doing all this, they maintain a determination to arrive at an original artistic or scientific expression."
    "We were given the example of Diana Dabby, a musician-turned-engineer."
    "She saw books written by engineers about the 'future of music', and wondered what kind of music would be made if she learned about engineering."
    "She went drom playing professional piano to enrolling in a New York City college to study electrical engineering."
    "She \"loved the adventure as much and frequently more than the treasure that her adventure was designed to bring her\"."
    "This phrase reminded me of Elizabeth Gilbert's talk on \"finding one's home\"."
    "Anyways, in Dabby's process, she made progress with hope of more progress to come."
    "... and then she went on to graduate school to study electrical engineering and computer science."
    "It turns out that one day, she drew a strange attractor with notes, and came up with a theory in just about five minutes."
    "But she couldn't have done that without the process of getting to that point."
    "... in short, artscience was a mechanism of idea translation, in which the process matters most."
    # PICTURE: Julio Ottino's work - watercolor?
    "The article then shifted focus to a painter named Julio Ottino."
    "He synthesized mathematics and painting."
    "Mainly, he expressed his frustration with his politically torn country of Argentina in his paintings."
    "In his doctoral on how certain fluids mixed, he approached the problem through pictures. He visualized the act of mixing."
    "He had a watercolor pasted on his desk that he looked at every day."
    "This led to his discovery that chaotic stretching and folding of fluid elements led to effective mixing."
    "Eventually, he became a teacher of fluid-mixing."
    "... and the article ended there."
    show sumner normal at center with dissolve
    s "In this article, we saw two artscientists realize their potential as artists while making important discoveries in the world of science."
    s "The most important part in pursuing artscience is the process."
    s "In turn, many important discoveries can be brought about by art-science."
    "..."
    s "That will be it for today. Class dismissed."
    
label week_5_4:
    # "The Philosophy of Creativity" by Paul and Kaufman
    show sumner normal at center with dissolve
    s "Good morning class."
    s "Today we will be reading yet an article about creativity."
    # I wish I was creative enough to get myself out of this mess
    "Like always, the article was handed out."
    "I looked down and read the title."
    "\"Introducing The Philosophy of Creativity\", by Elliot Samuel Paul and Scott Barry Kaufman."
    "We had to have the proper philosophy in order to be creative."
    "We must \"lose ourselves\" in what is beautiful."
    "Imagination is necessary for creativity; all our imagination does is manipulate the information found in the world."
    "Additionally, creativity is a reflection of character."
    "We are better at being creative when we rely on intrinsic motivation, rather than extrinsic."
    "Intrinsic motivation included pure love for the subject on which we were working on."
    "Extrinsic motivations were things like money, fame, and social status..."
    "In order to be creative, we must be interested, intrinsically, in something worthwhile."
    
label week_5_5:
    # assignment: paper on troubles you've had being "creative"
    show sumner normal at center with dissolve
    s "The assignment this week will be to write an essay on troubles you've had being \"creative\"."

label weekend_5:
    # weekend after 5th week

    
label week_6_1:
    # Mod 6: "We Who Are Creative"
    # RIP: A Remix Manifesto
    show sumner normal at center with dissolve
    # at this point, everything is breaking down
    p "... the past is trying to control the future by monetizing all digital media..."
    p "... but the information should be free ..."
    p "... we make new things by remixing..."
    p "... but the creators of the material want to make money out of it..."
    p "... the copyright law enforcement officer says... it doesn't matter if he's creative or not, if he's using other people's stuff..."
    p "... culture builds on the past ..."
    p "... copyright was designed to encourage people to create, not to hinder creation..."
    p "... in 18 months, we had assembled the largest library of human creativity ever, and had done it for free... and the corporations ruined that..."
    p "... the law made 52 million people copyright criminals ..."

label week_6_2:
    # Youtube: -- Posthuman: An Introduction to Transhumanism
    show sumner normal at center with dissolve
    # even more breaking down
    "... we are shackled by our primitive, Darwinian brains..."
    "... transhumanism... to fundamentally revolutionize what it means to be human by way of technological advancements..."
    "... three supers... super longevity... super intelligence... super well-being..."
    "... we are already in a symbiotic relationship with technology..."
    "... you can send your thoughts at incredible speeds to recipients on the other side of the planet, find your precise location using satellites, and access the world's repository of recorded human knowledge with the device you carry with you at all times..."
    

label finale:
    
    return
    

label end:
    #MC: Had always like comic books as a child; make visual novel
    "Whatever the outcome of this visual novel, I knew I would be wholly invested into it."
    play music music_end fadein 1.0
    scene bg park_night with dissolve
    show aura enthusiastic at left with dissolve
    show sumner glad at right with dissolve
    show dylan normal at center with dissolve
    #show randall glad
    #show mom normal
    $ aura_name = "Aura"
    a "Thanks for playing!"
    jump _credits
    
label _credits:
    scene black
    with Pause(1)

    show text "Credits..." with dissolve
    with Pause(2)
    
    show text "Sole developer: Aaron Huang" with dissolve
    with Pause(2)

    show text "Made with the Ren'Py visual novel engine." with dissolve
    with Pause(2)
    
    show text "For CLCS 1002 at the University of Connecticut" with dissolve
    with Pause(2)
    
    show text "Taught by professor Anke Finger." with dissolve
    with Pause(2)
    
    show text "... Thanks for playing!!!" with dissolve
    with Pause(360)
    hide text with dissolve


    return
    
# TEST SCENES FOR DEBUGGING #
label test_scene:
    $ aura_name = "Aura"
    $ sumner_name = "Yoyo"
    scene bg class_day with dissolve
    show sumner normal with dissolve
    s "HEYO"
    show origami at truecenter
    s "Cool picture huh?"
    s "AM I COOL OR WHAT."
    return

