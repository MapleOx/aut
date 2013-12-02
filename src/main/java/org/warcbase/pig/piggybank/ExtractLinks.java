package org.warcbase.pig.piggybank;

import java.io.IOException;
import java.util.List;

import org.apache.pig.EvalFunc;
import org.apache.pig.data.BagFactory;
import org.apache.pig.data.DataBag;
import org.apache.pig.data.Tuple;
import org.apache.pig.data.TupleFactory;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import com.google.common.collect.Lists;

public class ExtractLinks extends EvalFunc<DataBag> {
  private static final TupleFactory TUPLE_FACTORY = TupleFactory.getInstance();
  private static final BagFactory BAG_FACTORY = BagFactory.getInstance();
  
  public DataBag exec(Tuple input) throws IOException {
    if (input == null || input.size() == 0 || input.get(0) == null)
      return null;
    try {
      String str = (String) input.get(0);

      DataBag output = BAG_FACTORY.newDefaultBag();
      Document doc = Jsoup.parse(str);
      Elements links = doc.select("a[href]");

      for (Element link : links) {
        String target = link.attr("abs:href");
        if (target.length() == 0) {
          continue;
        }
        List<String> linkTuple = Lists.newArrayList();
        linkTuple.add(target);
        linkTuple.add(link.text());
        output.add(TUPLE_FACTORY.newTupleNoCopy(linkTuple));
      }
      return output;
    } catch (Exception e) {
      throw new IOException("Caught exception processing input row ", e);
    }
  }
}