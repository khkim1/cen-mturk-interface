/**
 * Final static values
 */
var colors = ["#FC8686", "#FFB566", "#DF97F7", "#97A9F7", "#97D6F7", "#77D4B9", "#F797C9", "#9FC482"];
// the photoIds should be populated from the database onload when setup is called.
var photoIds = [];

/**
 * Changing state values
 */
// maps photo (sorted by id) to its category number. 0 is uncategorized
var categorizedMap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
// houses copies of photo DOM elements for sorting/moving process
var photoCopies = [];
// The index of the next color category to be added. start at 4 since we will start off showing 4 categories
var nextColorInt = 2;
// currently selected int of the group
var currentlySelectedInt = null;

/**
 * called when the "add a group" button is called
 * adds a new color group button and an input field
 */
var addNewColor = function(){
  // cap the max number of groups by 8
  if (nextColorInt >= 9) {return;}
  
  var base = document.getElementById('baseColorRow');
  var newColorCategory = base.cloneNode(true);
  var newButton = newColorCategory.getElementsByTagName("button")[0];
  newButton.innerHTML = newName = "Group " + nextColorInt;
  newButton.style.backgroundColor = colors[nextColorInt - 1];
  newButton.onclick = function(newButton){
    selectColor(newButton);
  };
  document.getElementById('color-picker').appendChild(newColorCategory);
  var addButton = document.getElementById('addButton');
  if (nextColorInt == 8) {
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
  $(".color-button").removeClass("clicked");
  elem.className += " clicked";
  currentlySelectedInt = parseInt(elem.innerHTML.split("Group")[1]);
};

/**
 * called when an image is clicked.
 * colors the border appropriately
 */
var onImageClick = function(elem){

  if (currentlySelectedInt == null) {
    return;
  }
  imgName = elem.id;
  if (elem.style.borderColor == colors[currentlySelectedInt-1]) {
    elem.style.borderColor = "white";
    categorizedMap[parseInt(imgName)-1] = 0;
  } else {
    elem.style.borderColor = colors[currentlySelectedInt-1];
    categorizedMap[parseInt(imgName)-1] = (currentlySelectedInt);
  }
};

/**
 * Do any preloading set up here. this is called onload from the html
 */
var setup = function(imageNames) {
  photoIds = imageNames.splice(0).sort();
}

/**
 * called on click of the sort button. 
 * organize the photos by their categories.
 */
var sort = function() {
  savePhotoCopies();
  resetLists();
  debugger;
  for (var p = 0; p < 16; p++) {
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
  for (var p = 0; p < 16; p++) {
    photoCopies.push(document.getElementById(photoIds[p].toString()).cloneNode(true));
  }
};


var submit = function() {
// TODO: kunho. here, use categorizedMap and photoIds. they should map to each other: photoId to the category number.
// also export the descriptions that the users wrote.
};