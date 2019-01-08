# Notes for understanding react

### Why should you separate HTML/CSS/JS?
* **Efficiency of Code**: keep the files small, if you were to include styling and everything in one HTML file, then it would be very difficult to download all the files. 
* **Ease of maintenance**: If everything is in one place, things will get cluttered and it becomes difficult to pinpoint specific of a webpage without scrolling through a large page of code.
* **Accessibility**: Through a proper semantic structure, pages can be read to those who cannot see the webapage, hence, separating the text and images can help people who cannot see your website.
* **Device Compatibility**: Website is usually just plain markup (HTML/XHTML): the files need styling and styling can be different based on the given device: hence, one should use CSS or a separate styling sheet that makes the page scalable/compatible for any device.
* **Web Crawlers/Search Engines**: Want your page to be easily read through; hence, its useful to have all componenets of the page in a neat and orderly manner
* **It's just good practice**: generally the industry standards to separate each one.

### What is each of the three responsible for a webpage?
**HTML**: Basis of every page, decides which elements will be on the page. 
**CSS**: Styling of the HTML
**JS**: Adding behavior to the webpage by targeting a specific element in the HTML

### What is React?
* declarative, efficient, and flexible JS library for building UI
* Lets you compose complex UIs from small and isolated pieces of code called "components"

*React has several different components:*

* **`React.Component`**: has subclasses -> things that extend `react.component`:
	* Takes the parameters called props
	* Returns a hierarchy of views to disply via the `render` method
	* `render` method will return a *description* of what you want to see on the screen.
	* **React** Takes that *description* and displays that result. You can generally use "JSX" to make the structures easier to write.
	* JSX is something similar to JS, but is more structured and makes it seem like it is more of a template language than JS



### Differences between JSX and JS
*There comes ease with using JSX over JS*
	

**JS**
---
```javascript
class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}

// Example usage: <ShoppingList name="Mark" />
```

**JSX**
---
```javascript
React.createElement(
  "div",
  { className: "shopping-list" },
  React.createElement("h1", null, "Shopping List for ", props.name),
  React.createElement(
    "ul",
    null,
    React.createElement("li", null, "Instagram"),
    React.createElement("li", null, "WhatsApp"),
    React.createElement("li", null, "Oculus")
  )
);
```

### Understanding how Props work in React

**Original Code**
---
*Board Class*
```javascript
class Board extends React.Component {
  renderSquare(i) {
    return <Square />;
  }
```

*Square Class*
```javascript
class Square extends React.Component {
  render() {
    return (
      <button className="square">
        {/* TODO */}
      </button>
    );
  }
}
```

We get an image that then looks something like this:
![resulting image from previous code](https://reactjs.org/static/tictac-empty-1566a4f8490d6b4b1ed36cd2c11fe4b6-a9336.png)

**New Code**
---
*Board Class*
```javascript
class Board extends React.Component {
  renderSquare(i) {
    return <Square value={i} />;
  }
```

*Square Class*
```javascript
class Square extends React.Component {
  render() {
    return (
      <button className="square">
        {this.props.value}
      </button>
    );
  }
}
```

We then get an image that looks like this:
![resulting image from updated code](https://reactjs.org/static/tictac-numbers-685df774da6da48f451356f33f4be8b2-be875.png)

---

From this example, you can see how 'props' are passed down from parents to children

### Arrow Syntax
**Without Arrow**
---
*Square Class*
```javascript
class Square extends React.Component {
  render() {
    return (
      <button className="square" onClick={function() { alert('click'); }}>
        {this.props.value}
      </button>
    );
  }
}
```
**With Arrow**
---
```javascript
class Square extends React.Component {
 render() {
   return (
     <button className="square" onClick={() => alert('click')}>
       {this.props.value}
     </button>
   );
 }
}
```
---

In this case there is a difference in the following lines:

`<button className="square" onClick={() => alert('click')}>`

and 

`<button className="square" onClick={function() { alert('click'); }}>`

This is because, the prop for `onClick` is being passed as a function.

---

### What is **State**?

- State is a way for a componenet to remember that it was clicked.
- `this.state` - is generally used as the property of the componenet
- You can initialize the stage by using a `constructor`

### What does a **Constructor** look like? 

```javascript
  constructor(props) {
    super(props); // you always need this for any subclass 
    // hence every componenet in react needs a super(props)
    this.state = {
      value: null,
    };
  }
```     
- You can initialize the state of a given component.
- To change the state of the component: `this.setState({value: 'XXX'})}`
- To get the state of the componenet: `this.state.value`
*When you call `setState` in a component, React automatically updates the child componenets inside of it too*

### Managing multiple components at Once

- If you want to** get information** from two components or have two components **communicate** with each other you need to **lift the state** from the child components to the parent component
- Hence, the parent component in our case is the Board component

**Board Code**
```javascript
<Square
	value={this.state.squares[i]}
	onClick={() => this.handleClick(i)}
/>
```

**Square Code**
```javascript
<button
	className="square"
	onClick={() => this.props.onClick()}
>
```

**Order of events**
1. The `onClick` prop on the buil-in DOM `<button>` component tells React to set up a click event listener.
2. When the button is clicked, React will call the `onClick` handler that is defined in Square's `render()` method.
3. This event handler calls `this.props.onClick()`. The Square's `onClick` prop was specified by the board.
4. Since the Board passed `onClick={() => this.handleClick(i)}` to Square, the Square calls `this.handleClick(i)` when clicked
5. We have not defined the `handleClick()` so the code crashes

**React Conventions**
- `on[Event]` is generally used for props that **represent** events
- `handle[Event]` is generally used for methods which **handles** the events


**New Code**
In the new code: d18b9086e1ccb004174b4a8872095a2e5e94df4d
Compared to the code before it:

*Now the state is stored in the Board component instead of the individual Square components. When the Board's state changes, the Square components re-render automatically. Keeping the state of all squares in the Board components will allow it to determine the winner in the future.*

Square components no longer maintain their state -> the square components recieve values from the Board component and inform the Board that they've been clicked

Such a component that don't have its own state and reports to another component are called: **controlled components**

### Why the code uses `.slice()` everytime:

Two approaches to changing data:
- **Mutate**: directly change the values
- **Replace**: replace the data with a new copy of the data

Examples:

**Data Change with Mutation**:
---
```javascript
var player = {score: 1, name: 'Jeff'};
player.score = 2;
// Now player is {score: 2, name: 'Jeff'}
```

**Data Change without Mutation**:
```javascript
var player = {score: 1, name: 'Jeff'};

var newPlayer = Object.assign({}, player, {score:2});
// Now player is unchanged, but newPlayer is {score: 2, name: 'Jeff'}
```

**Benefits of Immutability**: 
- We are able to save specific states of the game and go through history.
- Helps you detect changes
- When to re-render in React -> helps you with creating *pure components*

---

## Function Components

- Change thee square to be a **Function Component**
- Simpler way to write omponents that only contain a `render` without a state
- Does not extend `React.Component`, instead writes a function that takes `props`

Hence, the new square code should look something like this:
```javascript
function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}
```
With a **Function Component**, there is no longer the need to use something that includes the `=>` or some other code that seems weird. 

### Taking Turns

We need to some how make a state that allows for the state of the game to realize who's turn it is.
Hence, we add a similar 

## Adding Time Travel

Store the state of the `squares` array in another array called `history`
We have to decide which component  will contain this array called `history`

### Lifting State Up, Again
*Considering the fact that the squares array is contained in the `board` class, the `history` should be contained in a hierarchially higher object*

- No longer need to keep the `squares` state in the Board Component. 
- Need to refractor the code so that the upper hierarchy absorbs all the exisitng classes in the bottom component.


### Showing the Past Moves

*React elements are first-class JS objects; we can pass them around in our applications*

Need to use a format like the following:

```javascript
const numbers = [1,2,3];
const doubled = numbers.map(x => x * 2); // [2,3,6]
```

With the code above you can do the following: 
- Map history of moves to React elements representing buttons on the screen and display a list of buttons to "jump" to past moves
- With new code in commit: 8b2c9ed56370110b0051de3adea63dc5e1388a36 
- You result with a warning:
  - *Warning: Each child in an array or iterator should have a unique "key" prop. Check the render method of "Game".*


**What does this warning mean?**
- When you update a list, React needs to determine what has changed. 

Transition from:
```javascript
<li>Alexa: 7 tasks left</li>
<li>Ben: 5 tasks left</li>
```

to 

```javascript
<li>Ben: 9 tasks left</li>
<li>Claudia: 8 tasks left</li>
<li>Alexa: 5 tasks left</li>
```
*Looks like we simply inserted Claudia in between Ben and Alexa*

React doesn't know what we wanted. Hence, you need to give each a specific key.

One option to fix this is to use strings `alexa`, `ben`, `claudia`

Hence it would look something like this:
```javascript
<li key = {user.id}>{user.name}: {user.taskCount} tasks left</li>
```

- **With keys:**
  - React takes each list item's key and searches the previous list's items for a matching key
  - If the current list has a key that didn't exist before, React creates a component
  - If the current list is missing a key that existed in the previous list, React destroys the previous component.
  - If the two keys match, the corresponding component is moved.
  - Keys tell React about the identity of each component which allows React to maintain state between re-renders

### More about Keys

- `key` is a special and reserved property in React
- When an element is created: React extracts the `key` property and stores the key directly on  the returned element

***STRONGLY RECOMMENDED THAT YOU ASSIGN PROPER KEYS WHENEVER YOU BUILD DYNAMIC LISTS.***

*If no key is specified, React will present a warning and use the array index as a key by default: this is problematic because when trying to re-order a list's items or inserting/removing list items*

Keys don't need to be globally unique, they only need to be unique between components and their siblings.




###
