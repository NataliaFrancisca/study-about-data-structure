// getProductSuggestions(['carpet', 'cart', 'car', 'camera', 'crate'], 'camera') 
// -> [['camera', 'car', 'carpet'], ['camera', 'car', 'carpet'], ['camera'], ['camera'], ['camera'], ['camera']]

function getProductSuggestions(products, search) {
    let arrSuggestions = [];
    let lastSugestion = products;

    for(let i = 0; i < search.length; i++){
        const mapFilter = lastSugestion.filter((word) => word[i] == search[i]);
        mapFilter.sort();
        if(mapFilter.length > 0){
            arrSuggestions.push(mapFilter.slice(0, 3));
        }
        lastSugestion = mapFilter;
    }
    
    return arrSuggestions;

}
