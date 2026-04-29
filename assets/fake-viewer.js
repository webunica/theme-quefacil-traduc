// Fake-viewers
var $fakeViewClass = $('.js-fake-view'),
    minValue = $fakeViewClass.data('min'),
    maxValue = $fakeViewClass.data('max'),
    duration = $fakeViewClass.data('duration');

// Function to update the fake view count
function updateFakeViewCount() {
  var value = Math.floor(Math.random() * (maxValue - minValue + 1)) + minValue;
  $fakeViewClass.text(value);
}

// Initialize the fake view counter and set up the interval
function initFakeViewCount() {
  updateFakeViewCount(); // Set initial random value
  if (minValue !== undefined && maxValue !== undefined && duration) {
    // Set an interval to update the view count at the specified duration (in milliseconds)
    setInterval(updateFakeViewCount, duration);
  }
}

// Run the initialization function
initFakeViewCount();
