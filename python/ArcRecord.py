# /*
#  * Archives Unleashed Toolkit (AUT):
#  * An open-source platform for analyzing web archives.
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *     http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  */

class ArcRecord(object):
  def __init__(self, contentBytes, contentString, crawlDate, crawlMonth, 
    domain, imageBytes, mimeType, url):
    self.contentBytes = contentBytes
    self.contentString = contentString
    self.crawlDate = contentString
    self.crawlMonth = crawlMonth
    self.domain = domain
    self.imageBytes = imageBytes
    self.mimeType = mimeType
    self.url = url

  def getCrawlDate(self): 
    return self.crawlDate

  def getMimeType(self):
    return self.mimeType

  def getUrl(self):
    return self.url 

  def getContentBytes(self):
    return self.contentBytes


  # val getCrawlMonth: String = ExtractDate(r.t.getRecord.getMetaData.getDate, DateComponent.YYYYMM)


  # val getDomain: String = ExtractDomain(r.t.getRecord.getMetaData.getUrl)

  # val getContentBytes: Array[Byte] = ArcRecordUtils.getBodyContent(r.t.getRecord)

  # val getContentString: String = new String(getContentBytes)

  # val getImageBytes: Array[Byte] = {
  #   if (getContentString.startsWith("HTTP/"))
  #     getContentBytes.slice(
  #       getContentString.indexOf(RemoveHttpHeader.headerEnd)
  #         + RemoveHttpHeader.headerEnd.length, getContentBytes.length)
  #   else
  #     getContentBytes
  # }

