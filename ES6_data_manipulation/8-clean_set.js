const cleanSet = (set, startString) => {
  const array = [];
  if (!startString) {
    return ``;
  }
  for (const element of set) {
    if (element.startsWith(startString) && typeof element === 'string') {
      array.push(element.slice(startString.length));
    }
  }
  return array.join('-');
}

export default cleanSet;
