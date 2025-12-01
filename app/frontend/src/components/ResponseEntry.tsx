const ResponseEntry = (results) => {
    results = results.results; // fixing funky response format
    return (
        <>
            <div className="flex flex-col gap-2">
                <span className="font-semibold">
                    Query ID: {results.query_id}
                </span>
                <div className="flex flex-col gap-2 py-2 w-fit rounded-xs mb-4">
                    <span className="underline decoration-2">
                        Cosine Similarity Results
                    </span>
                    {results.results.cosine_similarity.map((result) => (
                        <div className="flex flex-col gap-2 bg-neutral-600 ml-2 p-2 rounded-xs">
                            <span key={result.id} className="text-sm">
                                <span className="font-semibold">
                                    Embedding ID:
                                </span>{' '}
                                {result.id}
                            </span>
                            <span key={result.id} className="text-sm">
                                <span className="font-semibold">
                                    Similarity Score:
                                </span>{' '}
                                {result.score}
                            </span>
                            <span key={result.id} className="text-sm">
                                <span className="font-semibold">Text:</span>{' '}
                                <div className="pl-4">{result.text}</div>
                            </span>
                        </div>
                    ))}
                </div>

                <div className="flex flex-col gap-2 py-2 w-fit rounded-xs">
                    <span className="underline decoration-2">
                        Inner Product Results
                    </span>
                    {results.results.inner_product.map((result) => (
                        <div className="flex flex-col gap-2 bg-neutral-600 ml-2 p-2 rounded-xs">
                            <span key={result.id} className="text-sm">
                                <span className="font-semibold">
                                    Embedding ID:
                                </span>{' '}
                                {result.id}
                            </span>
                            <span key={result.id} className="text-sm">
                                <span className="font-semibold">
                                    Similarity Score:
                                </span>{' '}
                                {result.score}
                            </span>
                            <span key={result.id} className="text-sm">
                                <span className="font-semibold">Text:</span>{' '}
                                <div className="pl-4">{result.text}</div>
                            </span>
                        </div>
                    ))}
                </div>
            </div>
        </>
    );
};

export { ResponseEntry };
