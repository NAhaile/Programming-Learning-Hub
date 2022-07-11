# Questions from Quora 


Link: https://www.quora.com/How-do-the-best-programmers-write-programs-Do-they-reason-the-program-out-formally-on-paper-before-stepping-up-to-a-computer


These are just some QA's regarding programming I found interesting.

**Question**
*How do the best programmers write programs?*


**Answers 1 **
> **Disclaimer:** While I cannot claim to be one of “the best” programmers, I have known some much better than I am, but still I am confident that I am good enough that I am willing to be a proxy for the purposes of this question.

> Not generally. They will do that for key parts, but generally not large sections. Much of code is “boilerplate”. It’s code you have written dozens, possibly hundreds of times before. You write it out using idioms that you have used so often that you are almost on auto-pilot.

> However, you know that you make typographical errors and the code will interact with ones who aren’t careful, so you include assertions that validate that things are working as expected and you write unit tests to assure yourself that you didn’t write < when you meant <=.

> And the assertions you write will be sort of like a proof, You want to be able to show that the code will always work within the limits that you have laid down. And those limits will often be reflected in your unit tests. So, while you didn’t formally reason it out before hand, you have left enough breadcrumbs that if you need to debug it weeks, months, or even years later, that you will be able to do so then.

> But most of the code you write isn’t so complex that you need to reason it out formally. It is an extension, a variation on a theme, of the kind of code you know how to write. Yes, it may be a new combination of those parts, or solve a slightly different problem that you haven’t exactly solved before, but it will be close enough that you are applying well-known tools in your toolbox.

**An analogy:** You aren’t inventing the wheel not having seen something circular before, You are making a wheel that needs to fit on a lunar rover, but you have already done wheels on Ferraris and Semi trailers. You even have done wheels as part of tank treads. So, yes there are unique aspects to this problem, but you have a general idea of what it is going to look like. And, you know some of (not necessarily all of) the important factors, e.g. no air on the moon. sharp rocks. probably very cold. maybe very “sandy”—worry about that.

> So, if you were to look at the table near my desk with my laptops on them, you would see a pile of paper with some very sketchy notes on it. That’s things I want to implement and ideas I don’t want to forget. None of them are complete. They are just hints to myself. That’s what I need. Not completely formalized solutions. Just enough that I have captured the key points. And, yes some parts are more filled out than others.

> And, when you get to that level, you stop worrying about algorithm questions as part of an interview. One of two things will happen.

> 1. The question will be close enough to something you know how to do, that you can write out the answer on the “whiteboard”. It may not be a perfect solution. It may not use the absolutely optimal method, unless you happen to know it. But, it will work. It will be readable. You will be able to explain why you have solved the problem the way you did. You will probably even relate it to things you have done in your career and use the interview to highlight those while writing the code and tests. Yes, you will write tests as part of writing the code. That shows you are doing actual engineering, the way you will when working.

> 2. You won’t know how to solve the problem. Maybe you can get a hint to help you, but if not, you know the job isn’t one you should be taking anyway. You have limits. You know that faking it will only get you in trouble in the long run. 

-----------------------------------------------------------------------------------








