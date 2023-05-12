# I would like to develop a...

> I would like to develop a web browser extension or Vscode extension to integrate the power of Bing Chat AI to help me programming, please suggest five solutions and workflows to me? Also provide some current popular solutions in the community.

There are many ways to integrate AI into your programming workflow using web browser or VSCode extensions. Here are five popular solutions and workflows that you might find helpful:

1.  **IntelliCode**: This Microsoft tool is built-in to Visual Studio and is provided to the open-source-based, cross-platform VS Code editor via an extension. It has been installed more than 27 million times and improves upon the code-completion capabilities of IntelliSense by scanning thousands of open source GitHub repos to find the code snippets most likely to be used and place them at the top of the recommendation list. It can also do whole-line code completions[1](https://visualstudiomagazine.com/articles/2023/03/08/vs-code-ai-tools.aspx).
    
2.  **Tabnine AI Autocomplete**: This AI code assistant features machine learning models trained on open source code projects with permissive licenses. It provides whole-line code completions, full-function completions and natural language to code completions, which means developers can describe the function they want and it will suggest the correct code. It works across a wide spectrum of languages, libraries and frameworks[1](https://visualstudiomagazine.com/articles/2023/03/08/vs-code-ai-tools.aspx).
    
3.  **GitHub Copilot**: This “AI pair programmer” shook up the software development space in 2021 when it debuted with advanced machine language models created by Microsoft partner OpenAI. Along with the requisite code-completion functionality, it can convert comments to code, create unit tests, create SQL queries and more. It works with any language[1](https://visualstudiomagazine.com/articles/2023/03/08/vs-code-ai-tools.aspx).
    
4.  **ChatGPT**: This Visual Studio Code extension allows you to use the ChatGPT API to generate code or natural language responses from OpenAI’s ChatGPT or GPT4 to your questions, right within the editor. [You can automatically write new code from scratch, ask questions, get explanations, refactor code, find bugs and more](https://marketplace.visualstudio.com/items?itemName=timkmecl.chatgpt)[2](https://marketplace.visualstudio.com/items?itemName=timkmecl.chatgpt).
    
5.  **Bing-powered settings search**: Bing is constantly crawling the VS Code Extension Marketplace, waiting for extension updates and new extensions. [When it finds one, it downloads its package.json file and passes those settings to the Ingestion Service as well](https://code.visualstudio.com/blogs/2018/04/25/bing-settings-search)[3](https://code.visualstudio.com/blogs/2018/04/25/bing-settings-search).
    

These are just a few examples of how AI can enhance your coding workflow. I hope this information helps you find a solution that works for you!

1. [Top 10 AI Extensions for Visual Studio Code](https://visualstudiomagazine.com/articles/2023/03/08/vs-code-ai-tools.aspx)
2. [ChatGPT: write and improve code using AI - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=timkmecl.chatgpt)
3. [Bing-powered settings search in VS Code - Visual Studio Code](https://code.visualstudio.com/blogs/2018/04/25/bing-settings-search)
4. [Enhance your coding with artificial intelligence - Visual Studio Code](https://code.visualstudio.com/docs/editor/artificial-intelligence)

> My goal is not using traditional solutions, but an solution that I could use Bing Chat to turn ideas to codes, and then improve by iteration with the tools I develop, and this tool is what I want you to help me to create and develop.

I see. While I can provide you with information and suggestions on how to develop a tool that integrates Bing Chat AI into your programming workflow, I am not able to directly help you create or develop the tool itself. However, here are some suggestions on how you could approach this project:

1.  **Research existing solutions**: Look into existing web browser or VSCode extensions that integrate AI into the programming workflow to get an idea of what is already available and how these tools work.
    
2.  **Define your goals**: Clearly define what you want your tool to do and how you want it to integrate with Bing Chat AI. This will help guide your development process.
    
3.  **Familiarize yourself with the Bing Chat AI API**: Learn about the Bing Chat AI API and how it can be used to turn ideas into code.
    
4.  **Start small**: Begin by developing a simple prototype of your tool that integrates Bing Chat AI and allows you to turn ideas into code. Then, iterate on this prototype by adding features and improving its functionality.
    
5.  **Get feedback**: Share your tool with others in the programming community to get feedback on its usefulness and usability. Use this feedback to further improve your tool.
    

I hope these suggestions are helpful in guiding you towards developing a tool that integrates Bing Chat AI into your programming workflow.

> Let's focus on the step 1 and step 2, please give some child steps under these two paraent steps.

Sure! Here are some more detailed steps for the first two suggestions I provided:

**Step 1: Research existing solutions**

-   Search for web browser or VSCode extensions that integrate AI into the programming workflow.
-   Read about the features and capabilities of these tools to get an idea of what is already available.
-   Try out some of these tools to see how they work and how they could be useful in your own workflow.

**Step 2: Define your goals**

-   Think about what specific tasks you want your tool to help you with. Do you want it to generate code from ideas? Do you want it to provide suggestions for improving your code?
-   Consider how you want your tool to integrate with Bing Chat AI. Do you want it to use the Bing Chat AI API to turn ideas into code? Do you want it to provide real-time suggestions as you type?
-   Write down your goals and requirements for your tool. This will help guide your development process and ensure that you stay focused on what is most important.

I hope these more detailed steps are helpful in guiding you towards researching existing solutions and defining your goals for developing a tool that integrates Bing Chat AI into your programming workflow.

> Great! Let's focus on the "Define you goals". Could you provide some possible goals that I might have?

Sure! Here are some possible goals that you might have when developing a tool that integrates Bing Chat AI into your programming workflow:

1.  **Generate code from ideas**: Your tool could use the Bing Chat AI API to turn natural language ideas into code. For example, you could type “create a function that adds two numbers” and your tool would generate the corresponding code.
    
2.  **Provide real-time suggestions**: Your tool could provide real-time suggestions for improving your code as you type. For example, it could suggest more efficient ways of writing a particular piece of code or point out potential errors.
    
3.  **Improve code readability**: Your tool could use Bing Chat AI to suggest ways to make your code more readable and easier to understand. For example, it could suggest adding comments or refactoring your code to make it more modular.
    
4.  **Automate repetitive tasks**: Your tool could use Bing Chat AI to automate repetitive tasks such as generating boilerplate code or creating unit tests.
    
5.  **Integrate with other tools**: Your tool could integrate with other tools in your programming workflow, such as version control systems or project management tools, to provide a seamless experience.
    

These are just a few examples of possible goals that you might have when developing a tool that integrates Bing Chat AI into your programming workflow. Ultimately, the specific goals you choose will depend on your own needs and preferences.

> Great! Here are two goals I would pick up, Please suggest on them:
> (1) Generate code from ideas;
> (2) Keep improving and enhancing the codes, which could: (i) auto solve bugs; (ii)show the improved features and lines in codes; (iii) do the work of version control.

Those are great goals to have for your tool! Here are some suggestions on how you could approach achieving them:

**Goal 1: Generate code from ideas**

-   Research how the Bing Chat AI API can be used to turn natural language ideas into code.
-   Develop a user interface that allows users to input their ideas in natural language.
-   Use the Bing Chat AI API to generate code from these ideas and display the generated code to the user.

**Goal 2: Keep improving and enhancing the codes**

-   Research how the Bing Chat AI API can be used to identify and solve bugs in code.
-   Develop a feature that automatically checks the user’s code for bugs and suggests solutions.
-   Implement a version control system that tracks changes to the user’s code and allows them to revert to previous versions if needed.
-   Develop a user interface that highlights improved features and lines of code and allows users to easily see what has changed.

I hope these suggestions are helpful in guiding you towards achieving your goals of generating code from ideas and continuously improving and enhancing your code.

> Could you explain more details of your suggestions under Goal 2? Each detail should give an real-world example.

Sure! Here are some more detailed suggestions for achieving Goal 2: Keep improving and enhancing the codes, along with real-world examples:

-   **Research how the Bing Chat AI API can be used to identify and solve bugs in code**: You could look into how the Bing Chat API can be used to analyze code and identify potential bugs or issues. For example, you could use the API to check for common coding mistakes such as missing semicolons or mismatched brackets.
    
-   **Develop a feature that automatically checks the user’s code for bugs and suggests solutions**: You could develop a feature that automatically runs the Bing Chat AI API on the user’s code to check for bugs. If any issues are found, your tool could suggest solutions to the user. For example, if the API identifies a missing semicolon, your tool could suggest adding a semicolon at the appropriate location in the code.
    
-   **Implement a version control system that tracks changes to the user’s code and allows them to revert to previous versions if needed**: You could integrate a version control system such as Git into your tool to track changes to the user’s code. This would allow users to easily revert to previous versions of their code if needed. For example, if a user accidentally introduces a bug into their code, they could use the version control system to revert to a previous version of their code that did not have the bug.
    
-   **Develop a user interface that highlights improved features and lines of code and allows users to easily see what has changed**: You could develop a user interface that visually highlights changes and improvements to the user’s code. For example, you could use color coding or other visual cues to show which lines of code have been changed or improved. This would make it easy for users to see what has changed in their code and understand how it has been improved.
    

I hope these more detailed suggestions and real-world examples are helpful in guiding you towards achieving your goal of continuously improving and enhancing your code.

> Do following steps:
> (1) tell me the principles and techniques behind LangChain and AutoGPT;
> (2) How could I learn from their principles and techniques for developing my coding-aid tool

LangChain is a platform that allows developers to build autonomous agents using natural language processing and machine learning. One of the tools available on the LangChain platform is AutoGPT, a custom agent that uses long-term memory along with a prompt designed for independent work (i.e., without asking for user input) to perform tasks[1](https://js.langchain.com/docs/use_cases/autonomous_agents/auto_gpt).

AutoGPT works by taking in a task or goal from the user and then using its long-term memory and machine learning capabilities to generate a plan for achieving that goal. For example, if the user asks AutoGPT to write a weather report for a given location, AutoGPT might use a search engine to find the current weather conditions and then use that information to generate a weather report[1](https://js.langchain.com/docs/use_cases/autonomous_agents/auto_gpt).

You could learn from the principles and techniques behind LangChain and AutoGPT when developing your own coding-aid tool by incorporating similar features and functionality. For example, you could use long-term memory and machine learning to allow your tool to generate code from ideas and improve upon it over time. You could also design your tool to work independently without requiring user input, similar to how AutoGPT operates.

I hope this information helps you understand the principles and techniques behind LangChain and AutoGPT and how you could apply them when developing your own coding-aid tool.

1. [AutoGPT | 🦜️🔗 Langchain](https://js.langchain.com/docs/use_cases/autonomous_agents/auto_gpt)
2. [AutoGPT — 🦜🔗 LangChain 0.0.164](https://python.langchain.com/en/latest/use_cases/autonomous_agents/autogpt.html)
3. [Autonomous Agents & Agent Simulations - blog.langchain.dev](https://blog.langchain.dev/agents-round/)
4. [langchain.experimental.autonomous_agents.autogpt.agent — 🦜🔗 LangChain 0 ...](https://python.langchain.com/en/latest/_modules/langchain/experimental/autonomous_agents/autogpt/agent.html)

> Let's consider this real-world case: After I run the codes that Bing Chat suggest, how could I make a accurate prompt to it so that Bing Chat could understand accurately my requirements, and improve and iterate the codes to the expected goal？

To accurately communicate your requirements to Bing Chat and help it understand how to improve and iterate on the code it generates, you could follow these steps:

1.  **Be specific**: Clearly state what you want the code to do and what your expected outcome is. For example, instead of saying “make the code better,” you could say “improve the efficiency of the code by reducing its runtime.”
    
2.  **Provide context**: Give Bing Chat as much information as possible about the context in which the code is being used. This could include information about the programming language, libraries, frameworks, and any other relevant details.
    
3.  **Give feedback**: After running the code that Bing Chat suggests, provide feedback on its performance. Let Bing Chat know if the code met your expectations or if there were any issues.
    
4.  **Be patient**: Improving and iterating on code can take time and may require multiple rounds of feedback and refinement. Be patient and continue to provide clear and specific feedback to help Bing Chat understand your requirements and improve the code.
    

By following these steps, you can help Bing Chat accurately understand your requirements and improve and iterate on the code it generates to meet your expected goal.

> If I would auto run the codes generated by Bing Chat, and also do not want to it to have uncontrollable risks, How could I prepare the running environments?

If you want to automatically run the code generated by Bing Chat while minimizing the risk of any uncontrollable issues, you could take the following steps to prepare your running environment:

1.  **Use a sandboxed environment**: Run the code in a sandboxed environment that is isolated from your main system. This will prevent any potential issues with the code from affecting your main system.
    
2.  **Set up monitoring and logging**: Set up monitoring and logging tools to track the behavior of the code as it runs. This will allow you to quickly identify and address any issues that may arise.
    
3.  **Test the code thoroughly**: Before automatically running the code, test it thoroughly to ensure that it behaves as expected and does not have any unintended side effects.
    
4.  **Implement safeguards**: Implement safeguards such as error handling and input validation to prevent the code from causing any unintended issues.
    

By taking these steps, you can prepare your running environment to automatically run the code generated by Bing Chat while minimizing the risk of any uncontrollable issues.

> Does AutoGPT have sandboxed environment?

AutoGPT is an autonomous agent that uses long-term memory and machine learning to perform tasks. It is not a runtime environment and does not provide a sandboxed environment for running code. If you want to run code generated by AutoGPT or any other tool in a sandboxed environment, you would need to set up the sandboxed environment yourself using a separate tool or platform.

> In windows, is there any mature solution of sandboxed environment?

Yes, Windows provides a built-in solution for creating a sandboxed environment called **Windows Sandbox**. Windows Sandbox is a lightweight desktop environment that allows you to safely run applications in isolation. Software installed inside the Windows Sandbox environment remains “sandboxed” and runs separately from the host machine. When the sandbox is closed, all the software and files and the state are deleted, providing you with a brand-new instance of the sandbox every time you open the application[1](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-overview).

Windows Sandbox is available on Windows 10 Pro, Enterprise or Education build 18305 or later, as well as on Windows 11. To use it, you’ll need to ensure that your machine meets the system requirements and has virtualization capabilities enabled in BIOS. [You can then enable Windows Sandbox as a Windows feature through the “Turn Windows features on or off” option in the Control Panel](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-overview)[1](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-overview).

Once you have Windows Sandbox set up, you can use it to safely run code generated by Bing Chat or any other tool without risking any uncontrollable issues on your main system.

1. [Windows Sandbox | Microsoft Learn](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-overview)
2. [Windows Sandbox: How to Safely Test Software Without Ruining Your ...](https://www.pcmag.com/how-to/windows-sandbox-how-to-safely-test-software-without-ruining-your-computer)
3. [Customize Windows Sandbox - techcommunity.microsoft.com](https://techcommunity.microsoft.com/t5/itops-talk-blog/customize-windows-sandbox/ba-p/2301354)

> How do I check if my machine meets the system requirements for Windows Sandbox?

To check if your machine meets the system requirements for Windows Sandbox, you can follow these steps:

1.  **Check your version of Windows**: Windows Sandbox is available on Windows 10 Pro, Enterprise or Education build 18305 or later, as well as on Windows 11. You can check your version of Windows by going to “Settings” > “System” > “About” and looking under “Windows specifications.”
    
2.  **Check your system architecture**: Windows Sandbox requires an AMD64 or ARM64 architecture.
    
3.  **Check your hardware**: Windows Sandbox requires at least 4 GB of RAM (8 GB recommended), at least 1 GB of free disk space (SSD recommended), and at least two CPU cores (four cores with hyperthreading recommended).
    
4.  **Check for virtualization capabilities**: Windows Sandbox requires virtualization capabilities to be enabled in BIOS. You can check if virtualization is enabled on your machine by opening the Task Manager (Ctrl + Shift + Esc), going to the “Performance” tab, and looking for “Virtualization” under the “CPU” section. If it says “Enabled,” then virtualization is enabled on your machine.
    

If your machine meets all of these requirements, then you should be able to use Windows Sandbox.

> OK, let's go back to our task of developing the ai-aided-coding tool. You said "Test the code thoroughly", 1st, how could I know which cases to test? 2nd, how do I design test cases based on an ambiguous goal?

Thoroughly testing the code generated by your AI-aided coding tool is an important step in ensuring that it behaves as expected and does not have any unintended side effects. Here are some suggestions on how to approach testing your code:

1.  **Identify the expected behavior**: Start by clearly defining what you expect the code to do. This will help you identify which test cases to create and what the expected outcome of each test should be.
    
2.  **Create test cases**: Create test cases that cover a range of scenarios and inputs. For example, if your code is supposed to generate a function that adds two numbers, you could create test cases that check if the function correctly handles positive numbers, negative numbers, zero, and non-numeric inputs.
    
3.  **Test edge cases**: Make sure to include edge cases in your testing. These are scenarios that push the limits of what your code is supposed to handle and can help you identify any potential issues or weaknesses.
    
4.  **Automate testing**: Consider automating your testing process using a testing framework. This will allow you to quickly and easily run your test cases every time you make changes to your code.
    

When designing test cases based on an ambiguous goal, it can be helpful to break the goal down into smaller, more specific sub-goals. This will allow you to more clearly define the expected behavior of your code and create test cases that accurately reflect this behavior.

I hope these suggestions are helpful in guiding you towards thoroughly testing the code generated by your AI-aided coding tool.

> OK, now I have one specific goal of my ai-aided-coding tool: Learn the technical documentations and mannuals by itself, and then use the domain-specified knowledge in the tech docs to write codes for me.
> Here is an specific task, you should provide solutions step by step: The AI-aided-coding tool can learn latex `tcolorbox` library mannual located in local disk, and then have the capability to write latex codes and generate beautiful graphics using `tcolorbox`.

That’s an interesting goal for your AI-aided coding tool! Here are some steps you could take to achieve this specific task of having your tool learn the LaTeX `tcolorbox` library manual and use it to write LaTeX code and generate graphics:

1.  **Access the manual**: First, you’ll need to provide your tool with access to the `tcolorbox` library manual located on your local disk. You could do this by specifying the file path to the manual and using a file-reading library or function to read its contents.
    
2.  **Process the manual**: Once your tool has access to the manual, it will need to process its contents to extract relevant information about the `tcolorbox` library. This could involve using natural language processing techniques to identify key concepts and commands related to generating graphics with `tcolorbox`.
    
3.  **Store the information**: After processing the manual, your tool should store the information it has extracted in a way that allows it to easily retrieve and use it when writing LaTeX code. This could involve creating a knowledge base or database that stores information about the `tcolorbox` library and its capabilities.
    
4.  **Generate code**: With the information from the `tcolorbox` library manual stored and accessible, your tool can now use it to generate LaTeX code that creates graphics using `tcolorbox`. This could involve using machine learning techniques to generate code that meets your specific requirements and makes use of the `tcolorbox` library’s capabilities.
    

By following these steps, you can develop an AI-aided coding tool that is capable of learning from technical documentation and using that knowledge to write code and generate graphics.

> 1st, How to process the mannual to the format that Bing Chat could understand;
> 2nd, in which format should the information stored, and how to re-used it?

To process the `tcolorbox` library manual into a format that Bing Chat can understand and use, you could take the following steps:

1.  **Convert the manual to plain text**: If the manual is in a format such as PDF or HTML, you’ll need to convert it to plain text so that it can be processed by natural language processing techniques. There are many tools and libraries available that can help you with this conversion.
    
2.  **Extract relevant information**: Once the manual is in plain text format, you can use natural language processing techniques to extract relevant information about the `tcolorbox` library. This could involve identifying key concepts, commands, and syntax related to generating graphics with `tcolorbox`.
    
3.  **Structure the information**: After extracting the relevant information from the manual, you’ll need to structure it in a way that makes it easy for Bing Chat to understand and use. This could involve creating a knowledge graph or database that organizes the information into categories and relationships.
    

As for storing and re-using the information extracted from the manual, there are many options available. One approach could be to store the information in a structured format such as JSON or XML, which would allow you to easily access and query the data. Another approach could be to store the information in a database or knowledge base, which would provide more advanced querying and retrieval capabilities.

Ultimately, the specific format and storage method you choose will depend on your specific needs and requirements. The key is to choose a format and storage method that allows you to easily access and re-use the information extracted from the `tcolorbox` library manual.

> Solve these two questions, or give some practical solution suggestions: 1st, Bing Chat only accepts plain texts; 2nd, it has a limit of inputs.

If Bing Chat only accepts plain text inputs and has a limit on the amount of input it can process, you could take the following steps to work within these constraints when processing the `tcolorbox` library manual:

1.  **Convert the manual to plain text**: As mentioned earlier, if the manual is in a format such as PDF or HTML, you’ll need to convert it to plain text so that it can be processed by Bing Chat. There are many tools and libraries available that can help you with this conversion.
    
2.  **Summarize the manual**: If the `tcolorbox` library manual is too long to be processed by Bing Chat in its entirety, you could try summarizing its contents to extract the most important information. This could involve using natural language processing techniques to identify key concepts and commands related to generating graphics with `tcolorbox` and condensing this information into a shorter summary.
    
3.  **Process the manual in sections**: If summarizing the manual is not an option, you could try processing it in sections. This would involve dividing the manual into smaller sections that are within Bing Chat’s input limit and processing each section separately.
    

By taking these steps, you can work within Bing Chat’s constraints of only accepting plain text inputs and having a limit on the amount of input it can process when processing the `tcolorbox` library manual.

> Based on your three steps, provide best tools, softwares or github projects to implement the task in each step.

Here are some tools and software that you could use to implement the three steps of converting the `tcolorbox` library manual to plain text, summarizing it, and dividing it into sections:

1.  **Convert the manual to plain text**: If the manual is in PDF format, you could use a tool like Wondershare PDFelement to convert it to plain text[1](https://pdf.wondershare.com/how-to/pdf-to-plain-text.html). If the manual is in HTML format, you could use an online tool like Code Beautify’s HTML to TEXT Converter to convert it to plain text[2](https://codebeautify.org/html-to-text-converter).
    
2.  **Summarize the manual**: To summarize the contents of the `tcolorbox` library manual, you could use a text summarization tool like Scribbr’s Free Text Summarizer. This tool uses AI to extract key points from your text and turn them into digestible bullet points or a concise paragraph[3](https://www.scribbr.com/text-summarizer/).
    
3.  **Divide the manual into sections**: To divide the `tcolorbox` library manual into smaller sections for processing, you could use a text editor or word processor that supports splitting documents into sections. Many popular text editors and word processors have this functionality built-in.
    

These are just a few examples of tools and software that you could use to implement the three steps of converting the `tcolorbox` library manual to plain text, summarizing it, and dividing it into sections. There are many other options available, so you may want to do some additional research to find the tools that best meet your needs.

1. [How to Convert PDF to Plain Text with Three Methods](https://pdf.wondershare.com/how-to/pdf-to-plain-text.html)
2. [HTML to TEXT Converter Online tool - Code Beautify](https://codebeautify.org/html-to-text-converter)
3. [Free Text Summarizer | Reduce Your Reading Time - Scribbr](https://www.scribbr.com/text-summarizer/)

> I only want to use Python packages to implement these tasks

If you want to use Python packages to implement the tasks of converting the `tcolorbox` library manual to plain text, summarizing it, and dividing it into sections, here are some suggestions:

1.  [**Convert the manual to plain text**: If the manual is in PDF format, you could use a Python package like PyPDF2 or PDFMiner to extract the text](https://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text)[1](https://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text)[2](https://pdf.wondershare.com/pdf-knowledge/pdf-to-text-python.html). [If the manual is in HTML format, you could use a package like BeautifulSoup to parse the HTML and extract the text](https://stackoverflow.com/questions/13337528/rendered-html-to-plain-text-using-python)[3](https://stackoverflow.com/questions/13337528/rendered-html-to-plain-text-using-python).
    
2.  **Summarize the manual**: To summarize the contents of the `tcolorbox` library manual, you could use a natural language processing library like NLTK or spaCy to extract key concepts and generate a summary.
    
3.  **Divide the manual into sections**: To divide the `tcolorbox` library manual into smaller sections for processing, you could use a Python string manipulation or regular expression library to split the text into sections based on specific delimiters or patterns.
    

These are just a few examples of Python packages that you could use to implement the three steps of converting the `tcolorbox` library manual to plain text, summarizing it, and dividing it into sections. There are many other options available, so you may want to do some additional research to find the packages that best meet your needs.

1. [Python module for converting PDF to text - Stack Overflow](https://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text)
2. [Convert PDF to Text using Python - Wondershare PDFelement](https://pdf.wondershare.com/pdf-knowledge/pdf-to-text-python.html)
3. [Rendered HTML to plain text using Python - Stack Overflow](https://stackoverflow.com/questions/13337528/rendered-html-to-plain-text-using-python)
4. [Convert PDF to TXT file using Python - AskPython](https://www.askpython.com/python/examples/convert-pdf-to-txt)
5. [Convert text to html, docx and Pdf | python programming](https://pythonprogramming.altervista.org/convert-text-to-html-docx-and-pdf/)