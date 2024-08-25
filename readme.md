# 🍳 Chef GPT
Welcome to Chef GPT, a custom AI-powered model designed to assist with your culinary needs. This model can:

- 🥘 Ingredient-Based Dish Suggestions: Provide dish names based on the ingredients you have on hand.
- 🍲 Recipe Requests for Specific Dishes: Retrieve recipes for requested dishes.
- 🧑‍🍳 Recipe Critiques & Improvement Suggestions: Offer feedback and improvements on existing recipes.

Note: For requests based on ingredients, Chef GPT will suggest only dish names without providing the full recipes.

# 🛠 Installation and Setups

## Genral Setup
Please follow the steps below to install all relevant dependencies:

- Ensure to have an OpenAI API key from your [Playground account](https://platform.openai.com/settings/profile?tab=api-keys).

- Make sure you have `pip` installed on your system.

- Run the following command to install the required dependencies from the requirements.txt file:

- `pip install -r requirements.txt`

## Setting Up API

### Step 1: After Geeting Your API Key From Open AI 
 ```bash
   # Linux/MacOS/Bash on Windows
   export OPENAI_API_KEY="your-api-key-here"
   ```

   ```bash
   # Windows Command Prompt
   set OPENAI_API_KEY=your-api-key-here
   ```

   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="your-api-key-here"
   ```

 ### Step 2: Check if you have the variable set up correctly by running the following command on your terminal:

   ```bash
   # Linux/MacOS/Bash on Windows
   echo $OPENAI_API_KEY
   ```

   ```bash
   # Windows Command Prompt
   echo %OPENAI_API_KEY%
   ```

   ```bash
   # Windows PowerShell
   echo $env:OPENAI_API_KEY
   ```

 ### Step 3: To check if the key is set up correctly without revealing your key on your terminal, you can display it partially by running the following command:

   ```bash
   # Linux/MacOS/Git Bash on Windows
   echo ${OPENAI_API_KEY:0:3}...
   ```

   ```bash
   # Windows Command Prompt
   echo %OPENAI_API_KEY:~0,3%...
   ```

   ```bash
   # Windows PowerShell
   echo ($env:OPENAI_API_KEY).Substring(0,3) + "..."
   ```

### Step 4: Final Check

 Check if you have `sk-...` and not just `...`

> For more instructions on how to complete this in different Operational Systems, go to <https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key>

Now you're ready to start cooking with Chef GPT! 🍽️

# Contact 
Let me know if you need any more details or adjustments by reaching out to me on gregoryarthur98@gmail.com

