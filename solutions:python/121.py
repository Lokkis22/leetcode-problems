def maxProfit(prices):
        if len(prices) < 2:
            return 0

        minBuyPrice = 100000
        bestProfit = 0

        for i in range(len(prices)):
            if prices[i] - minBuyPrice > bestProfit:
                bestProfit = prices[i] - minBuyPrice
            
            if prices[i] < minBuyPrice:
                minBuyPrice = prices[i]
        
        return bestProfit