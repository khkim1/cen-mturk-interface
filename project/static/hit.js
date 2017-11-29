/**
 * Final static values
 */

// colors to be used on the screen 
var colors = ["#fc8686", "#ffb566", "#df97f7", "#97a9f7", "#97d6f7", "#77d4b9", "#f797c9", "#9fc482", "#ffd700", "#d2691e"];

// the photoIds should be populated from the database onload when setup is called.
var photoIds = [];

var num_images = 24;

var num_cat = 10; 

var group_descriptions = []; 

/**
 * Changing state values
 */
// maps photo (sorted by id) to its category number. 0 is uncategorized
var categorizedMap = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                      0, 0, 0, 0]; 

// houses copies of photo DOM elements for sorting/moving process
var photoCopies = [];
// The index of the next color category to be added. start at 2 since we will start off showing 1 categories
var nextColorInt = 2;
// currently selected int of the group
var currentlySelectedInt = null;

function rgb2hex(rgb){
 rgb = rgb.match(/^rgba?[\s+]?\([\s+]?(\d+)[\s+]?,[\s+]?(\d+)[\s+]?,[\s+]?(\d+)[\s+]?/i);
 return (rgb && rgb.length === 4) ? "#" +
  ("0" + parseInt(rgb[1],10).toString(16)).slice(-2) +
  ("0" + parseInt(rgb[2],10).toString(16)).slice(-2) +
  ("0" + parseInt(rgb[3],10).toString(16)).slice(-2) : '';
}

/**
 * called when the "add a group" button is called
 * adds a new color group button and an input field
 */
var addNewColor = function(){
  // cap the max number of groups by 8
  if (nextColorInt >= num_cat + 1) {return;}
  
  // Clone the original node 
  var base = document.getElementById('baseColorRow');
  var newColorCategory = base.cloneNode(true);
  var newButton = newColorCategory.getElementsByTagName("button")[0];
  var newText = newColorCategory.getElementsByTagName("input")[0]; 

  // Alter color and text id 
  newButton.innerHTML = newName = "Group " + nextColorInt;
  newButton.style.backgroundColor = colors[nextColorInt - 1];
  newButton.style.border = '5px solid transparent';
  newText.id = 'description' + nextColorInt;
  newText.value = '';

  newButton.onclick = function(newButton){
    selectColor(newButton);
  };

  selectColor(newButton);

  document.getElementById('color-picker').appendChild(newColorCategory);
  var addButton = document.getElementById('addButton');
  if (nextColorInt == num_cat) {
    addButton.disable = true;
    addButton.style.backgroundColor = "#BABABA";
  }
  nextColorInt++;
};

/**
 * called when a color category is clicked
 * sets the state to be that certain group color
 */
var selectColor = function(elem) {
  if (elem.type == 'click') {
    elem = elem.target;
  }

  var buttons = document.getElementsByClassName('color-button button');
  
  for (var i = 0; i < nextColorInt-1; i++) {
    buttons[i].style.borderColor = 'transparent'
  }

  elem.style.borderColor = "#001f3f";

  $(".color-button").removeClass("clicked");
  elem.className += " clicked";
  currentlySelectedInt = parseInt(elem.innerHTML.split("Group")[1]);
};

/**
 * called when an image is clicked.
 * colors the border appropriately
 */
var onImageClick = function(elem){

  var text = document.getElementById('description' + currentlySelectedInt).value;

  if (currentlySelectedInt == null) {
    return;
  }
  imgName = elem.id;

  if (rgb2hex(elem.style.borderColor) == colors[currentlySelectedInt-1]) {
    elem.style.borderColor = "transparent";
    categorizedMap[photoIds.indexOf(imgName)] = 0;
    //categorizedMap[parseInt(imgName)-1] = 0;
  } 
  else {
    elem.style.borderColor = colors[currentlySelectedInt-1];
    categorizedMap[photoIds.indexOf(imgName)] = (currentlySelectedInt);
  }
};

/**
 * Do any preloading set up here. this is called onload from the html
 */
var setup = function(imageNames) {
  if (! localStorage.justOnce) {
    localStorage.setItem("justOnce", "true");
    window.location.reload();
  }
  photoIds = imageNames.splice(0).sort();

  var base = document.getElementById('baseColorRow');
  selectColor(base.getElementsByTagName("button")[0]);

}

/**
 * called on click of the sort button. 
 * organize the photos by their categories.
 */
var sort = function() {
  savePhotoCopies();
  resetLists();
  debugger;
  for (var p = 0; p < num_images; p++) {
    var photo = photoCopies[p]
    document.getElementById('sortedList' + categorizedMap[p]).appendChild(photo);
  }
}

/**
 * Flush out all the photo objets from the categorized lists
 */
var resetLists = function() {
  var lists = document.getElementsByClassName("image-list");
  for (var l = 0; l < lists.length; l++) {
    while (lists[l].hasChildNodes()) {
      lists[l].removeChild(lists[l].lastChild);
    }
  }
};

/**
 * Clone the photo DOM objects before removing them during sort
 */
var savePhotoCopies = function() {
  debugger;
  photoCopies = [];
  for (var p = 0; p < num_images; p++) {
    photoCopies.push(document.getElementById(photoIds[p].toString()).cloneNode(true));
  }
};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

var submit = function(num_hits) {
// TODO: kunho. here, use categorizedMap and photoIds. they should map to each other: photoId to the category number.
// also export the descriptions that the users wrote.

  // Change this when want to expand the number of HITs 
  var num_hits_per_task = 10

  // Extract the group descriptions 
  for (var t = 1; t < nextColorInt; t++) { 
    group_descriptions.push(document.getElementById('description' + t).value)
  }

  // Get rid of the .png tag at the end of the file names
  for (var p = 0; p < num_images; p++) {
    photoIds[p] = photoIds[p].slice(0, -4)
  }

  // Send data to flask for processing
  $.post("/hit", {image_id_data: JSON.stringify(photoIds), 
    cluster_id_data: JSON.stringify(categorizedMap), 
    group_description_data: JSON.stringify(group_descriptions)});

  for (var counter = 0; counter < 500000000; counter++) {}

  // Decide redirect round based on current number of HITs completed 
  if (num_hits == num_hits_per_task - 1) { 
    window.location = "/"
  }
  else {
    window.location = '/hit'
  }

};








