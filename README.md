# data_structures_visualizer


This is an interactive full-stack wb application that visually demonstrates the behavior of core data structures and algorithms 
with the use case to be students, developers and interview prep by making it more hands-on and provide visuals for the user to learn and understand the concepts of.

Features:
- Stack and Queue 
  - the ability to push(enqueue), pop(dequeue), and peek in real time 
  
- Singly and Doubly Linked Lists
  - the ability to add to the head and the tail, delete from the head and tail, reverse the list with animation showing how the link list does it with current, next and end
  - provides their respected arrows direction 
  
- Binary Tree
  - the ability to insert, delete a specific node, get the height of the tree, the leaf node count and see it the tree is balance 
  - the ability to traverse in-order, pre-order and post-order with nodes being highlighted as it traverse 
  
- Sorting Algorithms 
  - Visualize bubble sort, insertion sort, selection sort, merge sort, and quick sort with step-by-step process
  
- Search and Filter
  - the ability to find data structures or algorithms based on name, description and rating(personal opinion)
  
- Accordion UI 
  - Clean and categorised layout so that the user can navigate the models with ease 

Tech Stack:
- Front End
  - React.js with Vite for development 
  - Material Ui for the UI
  - Framer Motion for animation 
  - Axios for API request 
  
- Backend 
  - FastAPI for Python backend 
  - Rest API for routes for each data structure and sorting algorithms 
  - Pydantic for data validation and schema modeling
  
- Deployment 
  - Vercel for Frontend 
  - Render FastAPI Server for backend 


How it Works: 
- Backend
  - a directory that has all the models(Stack,Queue, etc.) with individual files with their class and common function that you would use the data structures for or the functions to do the sorting 
  - the model directory connects to the routes directory that uses RestAPI routers to be the middle man for the FastAPI Backend to the model directory, using GET, POST and DELETE 
  - that gets connected to the main.py, where it runs the FastAPI backend, when data is sent, pydantic validates if the data is correct like int. 
  - for the main.py we use CORSMiddleware from FastAPI to allow the Frontend to make request to the Backend because they are on different domains
  
- Frontend 
  - the frontend is build using React.js with Vite, we use Reacts routers to navigate the visualizer page or the home page 
  - Axios is used to talk to the FastApi Backend, with it sending request to the backend 
  - Material UI was used for the buttons, cards typography, framer motion was for the animation like node transitions for highlighting during transversing and MUI Accordian was to organize the model on the home page 
  - the data of tha cards is sorted in a json file,
  - where it has an id,name,description of the data structure or algorithm, a rating, an image of the visualizer and the route for the React Router to call upon 


Live Demo: 
- Full Demo App: https://data-structures-visualizer-six.vercel.app/


Motivation: 
While learning how to code, I always struggled with how data structures and the sorting algorithms worked, yes I knew how to code them, but I never know how it did stuff, I need something, so I can visually see how they worked. Also, I'm a hands-on learner, I need to build something to reinforce these fundamentals for myself and also to help other to grasp these concepts. 


Future Enhancements:
- adding in red and black trees 
- adding hashmaps 
- adding tries 
- adding graphs 
- adding Breadth First Search(BFS) and Depth First Search(DFS)
- add all the time complexity to all the data structures and algorithms
- add space complexity to all the data structures and algorithms 
- add an AI Bot to further explain the concept to the user as well as answer common question that users may have 
- polish visualization and transitions for a smoother UX
