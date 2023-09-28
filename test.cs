[TestMethod]
public void TestMethod2()
{
    List<string> list1 = new List<string>() { "Tokyo", "Osaka", "Yokohama", "Nagoya", "Kobe" };
    List<string> list2 = new List<string>() { "Tokyo", "Yokohama", "Sapporo", "Fukuoka" };

    // 和集合（重複データは除かれる）を求めた後、文字列の昇順にソートする。
    System.Console.WriteLine("和集合＋昇順：" + string.Join(",", list1.Union(list2).OrderBy(cityName => cityName)));

    // 和集合（重複データは除かれる）を求めた後、文字列の降順にソートする。
    System.Console.WriteLine("和集合＋降順：" + string.Join(",", list1.Union(list2).OrderByDescending(cityName => cityName)));
}
