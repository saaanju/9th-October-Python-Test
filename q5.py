'''
A social media platform stores the number of likes received by five 
posts in a list. Write a function to find the post with the highest 
likes, calculate total likes, and display posts that received at least 
100 likes.
'''


def likes_calculate(likes_data):
    highest=max(likes_data)
    total_likes=sum(likes_data)
    print(f"highestl_liked_post={highest}")
    print(f"total_liked_post={total_likes}")
    
    for i in likes_data:
        if i >= 100:
            print(i)


likes_data=[10,20,30,500,450,234,100]
likes_calculate(likes_data)