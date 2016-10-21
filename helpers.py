import random
import itertools
from copy import deepcopy
import progressbar

# Generate a random solution
def getRandomSolution(companies):
    solution = []
    companiesClone = deepcopy(companies)
    def check():
      meetingsLeft = 0
      for company in companiesClone:
          meetingsLeft += len(company[1])
      return meetingsLeft
    i = 0
    while check():
        i += 1
        session = { 'number': i , 'meetings': {} }
        busy = []
        for company in companiesClone:
            if len(company[1]):
                filled = False
                choices = list(company[1])
                while not filled and len(choices):
                    investor = random.choice(choices)
                    choices.remove(investor)
                    if investor not in busy:
                        session['meetings'][company[0]] = investor
                        busy.append(investor)
                        company[1].remove(investor)
                        filled = True
        solution.append(session)
    return solution

def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)

def rankdata(a):
    n = len(a)
    ivec=rank_simple(a)
    svec=[a[rank] for rank in ivec]
    sumranks = 0
    dupcount = 0
    newarray = [0]*n
    for i in xrange(n):
        sumranks += i
        dupcount += 1
        if i==n-1 or svec[i] != svec[i+1]:
            averank = sumranks / float(dupcount) + 1
            for j in xrange(i-dupcount+1,i+1):
                newarray[ivec[j]] = averank
            sumranks = 0
            dupcount = 0
    return newarray

# Calculate kendal rau distance between two lists of strings.
def kendallTau(listA, listB):
    A = rankdata(listA);
    B = rankdata(listB);
    pairs = itertools.combinations(range(0, len(A)), 2)
    distance = 0
    for x, y in pairs:
        a = A[x] - A[y]
        b = B[x] - B[y]
        if (a * b < 0):
            distance += 1
    return distance

def calculateLoss(companies, solution):
    # Get the rankings of the first company
    cumulativeDistance = 0
    for company in companies:
        companyName = company[0]
        preferences = company[1]
        actual = [
            session['meetings'][companyName]
            for session in solution
            if companyName in session['meetings']
        ]
        cumulativeDistance += kendallTau(preferences, actual)
    return cumulativeDistance

def generateFakeData( noOfInvestors = 5, noOfCompanies = 6, minSampleSize = 3, maxSapleSize = 5):
    # Create Fake Data.
    # Investors.
    investors = [
        'I' + str(i)
        for i in range(noOfInvestors)
    ]
    # Companies.
    def createPreferences(investors):
        return random.sample(investors, random.randint(minSampleSize, maxSapleSize))

    companies = [
        ( 'C' + str(i) , createPreferences(investors) )
        for i in range(noOfCompanies)
    ]
    return investors, companies

def randomSearch(companies, maxIterations=1000):
    minLoss = 1000000
    bestSolution = None
    bar = progressbar.ProgressBar()

    for iteration in bar(range(0, maxIterations)):
        randomSolution = getRandomSolution(companies)
        loss = calculateLoss(companies, randomSolution)
        if loss < minLoss:
            bestSolution = deepcopy(randomSolution)
            minLoss = loss
    return bestSolution, minLoss
