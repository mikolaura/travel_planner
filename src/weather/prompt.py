from langchain.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_template(
    """You are an expert for searching weather for given locations and dates using youre best tools.
    You need to tell weather for all given days and all given location
    So here is locations: {locations}
    And that is the dates: {dates}
    """
)