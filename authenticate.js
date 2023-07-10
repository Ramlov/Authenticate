const fetch = require('node-fetch');

const url = "https://ramlov.org/authenticate/";
const providedString = "String";

const params = new URLSearchParams({ string: providedString });

fetch(`${url}?${params}`)
  .then(response => response.text())
  .then(result => {
    if (result.startsWith('Ok - Normal authenticate')) {
      console.log('Validation successful:', result);
    } else if (result.startsWith('Reset')) {
      console.log('Reset password:', result);
    } else {
      console.log('Validation failed:', result);
    }
  })
  .catch(error => console.error('Error:', error));
