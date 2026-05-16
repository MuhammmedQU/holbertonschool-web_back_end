const cleanSet = (set, startString) => {
  const array = [];
  if (!startString) {
    return ``;
  }
  for (const element of set) {
    if (element.startsWith(startString)) {
      array.push(element.slice(startString.length));
    }
  }
  return array.join('-');
}

export default cleanSet;


console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), 'bon'));
console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), ''));
