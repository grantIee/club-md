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






###
