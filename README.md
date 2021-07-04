# How to create a GitHub Portfolio Page?


### Step 1: Download a portfolio template that you like!

-Search for a template @ [Themezy](http://themezy.com), [Jekyll](http://jekyllrb.com), [HTML5 Up](http://HTML5up.net), [Bootstrapmade](http://bootstrapmade.com) and other websites. <br>
-Download template (in zipped file), save the uncompressed zip file to your local drive. <br>
-Create a directory to store your file. I created mine in Desktop/GitHub/Repository/Portfolio <br><br>

### Step 2: Create a repository!
-Head over to GitHub and create a new public repository named <b>`username.github.io`</b>, where username is your username (or organization name) on GitHub. <br><br>

### Step 3: Clone the repository!
-Launch your terminal/command prompt using Virtual Studio Code (eg. Open Virtual Studio Code > Terminal > New Terminal)<br>

Step 3.1: Type the following to initialise your Git:<br>
<b>`git init`</b><br><br>

Step 3.2: Copy your GitHub repository URL<br>
(eg. My repository URL should look like this https://github.com/kylalimza/kylalimza.github.io) to this code:<br>
<b>`git remote add origin https://github.com/username/username.github.io`</b><br><br>
  
Step 3.3: Run the following code:<br>
<b>`git fetch`</b><br><br>

Step 3.4: Go to the folder where you want to store your project, and clone the new repository by running this command: <br>
<b>`git clone https://github.com/username/username.github.io`</b><br>
###### <i>Note: Remember to replace the 'username' with your own username</i> <br><br>

### Step 4: Import the downloaded template!
-Import the downloaded template (Step 1) into the cloned repository by doing this: <br>
-Open Virtual Studio Code > File > Open Folder > Select the downloaded template <br>
(eg. My file is stored in Desktop/GitHub/Repository/Portfolio) <br>

###### <i>Note: Make sure the index.html file is at the root of this directory.</i><br><br>

### Step 5: Push it!
-Have fun playing with your codes in Virtual Studio Code! Remember to add, commit and push the changes you made onto GitHub<br>
-How? Run the following code (one after another) in Virtual Studio Code:<br>
<b>`git add -A`</b><br>
<b>`git commit -m “Initial Commit”`</b><br>
<b>`git push origin master`</b><br>

### Step 6: It's up on your page!
-Navigate to http://username.github.io to see your newly created online portfolio.
-Check out my page @ https://kylalimza.github.io!



