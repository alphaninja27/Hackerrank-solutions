select city
    from station where SUBSTRING(city,1,1) in ('A','E','I','O','U') and 
    SUBSTRING(city,-1,1) in ('A','E','I','O','U');
