def get_tweet_data(card):
    username = card.find_element_by_xpath('.//span').text
    handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    try:
        postdata = card.find_element_by_xpath('//time').get_attribute('datetime')
    except NoSuchElementException:
        return
    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    text = comment + responding
    reply_count = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet_count = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    likes_count = card.find_element_by_xpath('.//div[@data-testid="like"]').text
    
    tweet = (username, handle, postdata, text, reply_count, retweet_count, likes_count)
    
    return tweet


