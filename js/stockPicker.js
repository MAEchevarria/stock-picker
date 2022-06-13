exports.picker = function(prices) {
    let priceList = prices;
    let listOfDays = [];
    let profits = 0;
    let tempProfits = 0;

    for (let i = 0; i < priceList.length; i++){
        for (let j = i + 1; j < priceList.length; j++){
            if ((priceList[j] - priceList[i]) > tempProfits) {
                tempProfits = priceList[j] - priceList[i];
            }
                if (tempProfits > profits) {
                    profits = tempProfits;
                    listOfDays = [i, j];
                }
        }
    }
    return listOfDays;

}

