describe('Integration test', () => {
    it('Test connection with backend', () => {
      cy.request('POST', 'http://localhost:5000/', { sentence: 'test' })
       .should((response) => {
        expect(response.status).to.eq(200)
     })
    })
  });