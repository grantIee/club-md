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


# Differences between JSX and JS
*There comes ease with using JSX over JS*

<div style="-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;">
    <div style="display: inline-block;">
        <h2>JS</h2>
        <pre><code class="javascript">
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
</code></pre>
    </div>

    <div style="display: inline-block;">
        <h2>JSX</h2>
        <pre><code class="javascript">
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
</code></pre>
    </div>
</div>
	