const fetch = require('node-fetch');

async function authenticate(providedString) {
  const url = "https://website.website/";

  const params = new URLSearchParams({ string: providedString });

  const response = await fetch(`${url}?${params}`);
  const result = await response.text();

  if (result.startsWith('Ok - Normal authenticate')) {
    return 'Validation successful: ' + result;
  } else if (result.startsWith('Reset')) {
    /*Reset something*/
    return 'Reset: ' + result;
  } else {
    return 'Validation failed: ' + result;
  }
}

module.exports = {
  authenticate
};
