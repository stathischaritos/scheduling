from helpers import getRandomSolution, calculateLoss, generateFakeData, randomSearch
noOfInvestors = 20
noOfCompanies = 60
minSampleSize = 3
maxSapleSize = 5

investors, companies = generateFakeData(
    noOfInvestors= noOfInvestors,
    noOfCompanies= noOfCompanies,
    minSampleSize= minSampleSize,
    maxSapleSize = maxSapleSize
)

# Do N random searches and get best result.
N = 1000
bestSolution, minLoss = randomSearch(companies, maxIterations= N)

# Print best result
print bestSolution, minLoss
