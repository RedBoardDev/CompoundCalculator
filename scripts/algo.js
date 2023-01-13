function round(value, precision) {
    const multiplier = 10 ** precision;
    return Math.round(value * multiplier) / multiplier;
}

function convertOptiTime(minutes) {
	var years = Math.floor(minutes / 525600);
	minutes = minutes % 525600;
	var days = Math.floor(minutes / 1440);
	minutes = minutes % 1440;
	var hours = Math.floor(minutes / 60);
	minutes = minutes % 60;
	var leapYears = Math.floor((years) / 4);
	var month = Math.floor(((days + leapYears) * 12) / 365);
	var result = "";
	if (years > 0) {
	    result += round(years, 0) + (years === 1 ? " an, " : " ans ");
	}
	if (month > 0) {
	    result += round(month, 0) + (month === 1 ? " mois, " : " mois ");
	}
	if (days > 0) {
	    result += round(days , 0)+ (days === 1 ? " jour, " : " jours ");
	}
	if (hours > 0) {
	    result += round(hours, 0) + (hours === 1 ? " heure, " : " heures ");
	}
	if (minutes > 0) {
	    result += round(minutes, 0) + (minutes === 1 ? " minute" : " minutes");
	}
	return result;
}

function calculateNbrsOfPeriods(everyXfrequency) {
	let coefFrequency = 1440;
    const nbrsOfPeriods = 365 * (coefFrequency / everyXfrequency);
    return nbrsOfPeriods;
}

function calculateGrossRewards(nbrsOfPeriods, gasCost, APR, initialInvestment) {
	const interet = (1 + ((APR / 100) / nbrsOfPeriods)) ** nbrsOfPeriods - 1;
    return (interet * initialInvestment - gasCost * nbrsOfPeriods);
}

function calculateOptimumCompoundTime(gasCost, APR, initialInvestment) {
	let optimumCompoundTime = 0.01;
	let grossRewards = -1;
	let ActualGrossRewards = 0;
	let nbrsOfPeriods = 0;
	const LIMITE = 1000000;

	for (let i = 0.01; i < LIMITE; i += 1) {
    	nbrsOfPeriods = calculateNbrsOfPeriods(i);
      	ActualGrossRewards = calculateGrossRewards(nbrsOfPeriods, gasCost, APR, initialInvestment);
      	if (ActualGrossRewards > grossRewards) {
        	grossRewards = ActualGrossRewards;
        	optimumCompoundTime = i;
      	}
	}
  	return (optimumCompoundTime);
}

const gasCost = 0.03;
const APR = 32;
const initialInvestment = 6582;
console.log("gasCost:", gasCost);
console.log("APR:", APR);
console.log("initialInvestment:", initialInvestment);
console.log("\n");


const optimumCompoundDays = calculateOptimumCompoundTime(gasCost, APR, initialInvestment);
console.log("optimumCompoundDays", optimumCompoundDays);

const optimumNbrsOfPeriods = calculateNbrsOfPeriods(optimumCompoundDays);
const optimumGrossRewards = calculateGrossRewards(optimumNbrsOfPeriods, gasCost, APR, initialInvestment);
console.log("optimumGrossRewards", optimumGrossRewards, "$");

console.log(convertOptiTime(optimumCompoundDays));

